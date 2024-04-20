from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Guest_list, Reservations
from .forms import ReservationsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime, date
from django.db.models import Q
from django.urls import reverse
from datetime import date


def get_available_tables_for_today():
    """
    This function is there to show how many available 
    bookings are available to book for today.
    """
    
    today = date.today()
    booked_tables = Reservations.objects.filter(date=today).count()
    total_tables = 35
    available_tables = total_tables - booked_tables

    return available_tables

class ReservationsList(generic.ListView):
    model = Reservations
    template_name = "index.html"


class ReservationsDetail(View):
    """
    The ReservationsDetail class includes reservations 
    that the user has booked into.
    """

    template_name = 'reservations_detail.html'


    def get_queryset(self):
        return Reservations.objects.filter(user=self.request.user)

    def get(self, request):
        if request.user.is_authenticated:
            reservations = (
                Reservations.objects
                .filter(user=request.user)
                .order_by('date')
            )
            context = {
                    'reservations': reservations,
            }
            return render(request,"reservations_detail.html", context)
        else:
            messages.error(
                request,
                'Log in first to view your bookings.'
            )
            return redirect('login')


class MakeReservations(View):
    """
    The MakeReservations class exists to make a reservation
    on dates that are available.
    """

    template_name = 'make_reservation.html'
    total_tables = 5
    max_bookings_per_time = 5

    def get_available_slots(self, date):
        """
        This function exists to show the user options 
        to book in the times available in the option: TIME_CHOICES.
        """

        available_slots = []

        for time_choice, _ in Reservations.TIME_CHOICES:
            time = time_choice
            booked_tables = (
                Reservations.objects
                .filter(date=date, time=time)
                .count()
            )
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))

        return available_slots

    def get(self, request):
        """
        This function exists to show the user which date 
        they can make a reservation on and that the ReservationsForm
        should be used.
        """

        current_date = datetime.now().date()
        form = ReservationsForm()
        available_slots = []
        available_tables = get_available_tables_for_today()

        for time_choice in Reservations.TIME_CHOICES:
            time = time_choice[0]
            booked_tables = Reservations.objects.filter(date=current_date,
                                                         time=time).count()
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))

        context = {
            'form': form,
            'available_tables': available_tables,
            'available_slots': available_slots,
        }
        return render(request, 'make_reservation.html', context)

    def post(self, request):
        """
        This function exists to inform the user that if the form is filled 
        correctly, it will lead to reservation_detail, otherwise messages 
        will appear informing otherwise.
        """

        form = ReservationsForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                reservation = form.save(commit=False)

                if reservation.date < date.today():
                    messages.error(
                        request,
                        'Sorry, but you can not book a table for this day.'
                    )
                    return redirect('make_reservation')

                booked_tables_on_reservation_date = (
                    Reservations.objects
                    .filter(date=reservation.date, time=reservation.time)
                    .count()
                )

                if (booked_tables_on_reservation_date >=
                        self.max_bookings_per_time):
                    messages.error(
                        request,
                        'Sorry, but it is not more tables avaliable.'
                    )
                    return redirect('update_reservation')

                available_slots = self.get_available_slots(reservation.date)

                context = {
                    'form': form,
                    'available_slots': available_slots,
                }

                reservation.user = request.user
                reservation.approved = False
                reservation.save()
                request.session['online_booking_id'] = reservation.id
                messages.success(
                    request,
                    'Your booking is complete. Please wait for approval'
                )
                return redirect('reservations_detail')
            else:
                messages.error(request, 'Please, try again and look if something is missing.')
        else:
            messages.error(request, 'Log in first to view your bookings.')

        context = {
            'form': form,
        }
        return render(request, 'make_reservation.html', context)


class UpdateReservation(View):
    """
    The UpdateReservation class exists to be able to change made reservation.
    """

    template_name = 'update_reservation.html'
    total_tables = 5
    max_bookings_per_time = 5

    def get(self, request, pk):
        """
        This function exists to show that the ReservationsForm
        should be used.
        """
        reservation = get_object_or_404(Reservations, pk=pk)

        if reservation.user == request.user:
            form = ReservationsForm(instance=reservation)
            context = {
                'form': form,
                'reservation': reservation,
            }
            return render(request, 'update_reservation.html', context)
        else:
            messages.error(request, 'You are not authorized to update this booking.')
            return redirect('reservations_detail')

    def post(self, request, pk):
        """
        This function exists to inform the user that if the form is filled 
        correctly, it will lead to reservation_detail, otherwise messages 
        will appear informing otherwise.
        """
        reservation = get_object_or_404(Reservations, pk=pk)

        if reservation.user == request.user:
            form = ReservationsForm(request.POST, instance=reservation)
            if form.is_valid():
                new_reservation = form.save(commit=False)

            if new_reservation.date < date.today():
                messages.error(
                    request,
                    'Sorry, but you cannot update the reservation to a past date.'
                )
                return redirect('update_reservation', pk=pk)

            booked_tables_on_reservation_date = (
                    Reservations.objects
                    .filter(date=reservation.date, time=reservation.time)
                    .count()
                )

            if (booked_tables_on_reservation_date >=
                    self.max_bookings_per_time):
                messages.error(
                    request,
                    'Sorry, but it is not more tables avaliable.'
                )
                return redirect('make_reservation')

            new_reservation.save()
            new_reservation.approved = False
            messages.success(request, 'Your booking has been updated.')
            return redirect('reservations_detail')
        else:
            messages.error(request, 'Wrong! Please, try again.')

        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'update_reservation.html', context)


class DeleteReservation(View):
    """
    This function exists to delete a reservation.
    """

    def post(self, request, pk):
        reservation = get_object_or_404(Reservations, pk=pk)
        reservation.delete()
        messages.success(request, 'Your booking has been deleted.')
        return redirect('reservations_detail')


