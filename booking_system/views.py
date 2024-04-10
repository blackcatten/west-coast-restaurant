from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Guest_list, Reservations
from .forms import ReservationsForm


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
                    'reservations': reservations, 'reservations_form': ReservationsForm()
                }
            return render(
            request,
            "reservations_detail.html", context
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
            return redirect('reservations_detail')
        else:
            return render(request, "reservations_list", {"reservations_form": reservations_form})

      
class CreateReservations(View):
    template_name = 'create_reservations.html'

    def get(self, request):
        reservations_form = ReservationsForm()
        return render(request, self.template_name, {'reservations_form': reservations_form})

    def post(self, request):
        reservations_form = ReservationsForm(data=request.POST)
        if reservations_form.is_valid():
            reservations = reservations_form.save(commit=False)
            reservations.user = request.user
            reservations.save()
            return redirect('reservations_list')
        else:
            return render(request, self.template_name, {"reservations_form": reservations_form})

