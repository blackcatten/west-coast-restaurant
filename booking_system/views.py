from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Guest_list, Reservations
from .forms import ReservationsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime, date
from django.db.models import Q


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
                'You need to log in to view your bookings.'
            )
            return redirect('login')


class MakeReservations(View):

    template_name = 'make_reservation.html'
    total_tables = 10
    max_bookings_per_day = 10

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

        for time_choice in Reservations.TIME_CHOICES:
            time = time_choice[0]
            booked_tables = Reservations.objects.filter(date=current_date,
                                                         time=time).count()
            remaining_slots = self.total_tables - booked_tables
            if remaining_slots > 0:
                available_slots.append((time, remaining_slots))

        context = {
            'form': form,
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
                        'You cannot book a table for a past date.'
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
                        'No more tables available for'
                        ' the selected date and time.'
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
                    'Reservation request submitted successfully.'
                    'Your booking is pending approval.'
                )
                return redirect('reservations_detail')
            else:
                messages.error(request, 'Error in filling out the form.')
        else:
            messages.error(request, 'You need to log in to make a booking.')

        context = {
            'form': form,
        }
        return render(request, 'make_reservation.html', context)

