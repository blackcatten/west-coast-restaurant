from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Guest_list, Reservations
from .forms import ReservationsForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages


class ReservationsList(generic.ListView):
    model = Reservations
    template_name = "index.html"


class MakeReservations(View):

    template_name = 'make_reservation.html'

    def get(self, request):
        if request.user.is_authenticated:
            reservations = (
                    Reservations.objects
                    .filter(user=request.user)
                    .order_by('date')
                )
            context = {
                    'reservations': reservations, 'reservations_form': ReservationsForm()
                }
            return render(
            request,
            "make_reservation.html", context
            )
        else:
            messages.error(
                request,
                'You need to log in to view your bookings.'
            )
            return redirect('login')
        



    def post(self, request):

        reservations_form = ReservationsForm(data=request.POST)

        if reservations_form.is_valid():
            reservations = reservations_form.save(commit=False)
            reservations.user = request.user
            reservations.save()
            return redirect('reservation_detail')
        else:
            return render(request, "make_reservations", {"reservations_form": reservations_form})


class ReservationsDetail(View):
    template_name = 'reservations_detail.html'

    def get(self, request, pk):
        reservation = Reservations.objects.get(pk=pk)
        return render(request, self.template_name, {'reservation': reservation})    
