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

    
    today = date.today()
    booked_tables = Reservations.objects.filter(date=today).count()
    total_tables = 35
    available_tables = total_tables - booked_tables

    return available_tables

class ReservationsList(generic.ListView):
    model = Reservations
    template_name = "index.html"


class ReservationsDetail(View):

    template_name = 'reservations_detail.html'

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

    template_name = 'make_reservation.html'
    total_tables = 5
    max_bookings_per_day = 5

    def get_available_slots(self, date):

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
                        self.max_bookings_per_day):
                    messages.error(
                        request,
                        'Sorry, but it is not more tables avaliable.'
                    )
                    return redirect('make_reservation')

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

    def get(self, request, pk):
        reservation = get_object_or_404(Reservations, pk=pk)
        form = ReservationsForm(instance=reservation)
        context = {
            'form': form,
            'reservation': reservation,
        }
        return render(request, 'update_reservation.html', context)

    def post(self, request, pk):
        reservation = get_object_or_404(Reservations, pk=pk)
        form = ReservationsForm(request.POST, instance=reservation)

        if form.is_valid():
            new_reservation = form.save(commit=False)

            if new_reservation.date < date.today():
                messages.error(
                    request,
                    'Sorry, but you cannot update the reservation to a past date.'
                )
                return redirect('update_reservation', pk=pk)

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

    def post(self, request, pk):
        reservation = get_object_or_404(Reservations, pk=pk)
        reservation.delete()
        messages.success(request, 'Your booking has been deleted.')
        return redirect('reservations_detail')


