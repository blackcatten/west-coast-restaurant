from django.shortcuts import render
from django.views import generic, View
from .models import Guest_list, Reservations
from .forms import ReservationsForm


class ReservationsList(generic.ListView):
    model = Reservations
    template_name = "index.html"


class ReservationsDetail(View):

    template_name = 'reservations_detail.html'

    def get(self, request):
        reservations = Reservations.objects.all()
        context = {
                'reservations': reservations,
            }

        return render(
            request,
            "reservations_detail.html", context
        )



    def post(self, request):

        form = ReservationsForm(request.POST)

        if reservations_form.is_valid():
            reservations_form.instance.name = request.user.username
            reservations = reservations_form.save(commit=False)
            reservations.post = post
            reservations.save()
            return redirect('reservations_list')
        else:
            return render(request, "reservations_detail.html", {"form": form})

