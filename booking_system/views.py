from django.shortcuts import render
from django.views import generic
from .models import Guest_list, Reservations


class ReservationList(generic.ListView):
    model = Reservations
    queryset = Reservations.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

