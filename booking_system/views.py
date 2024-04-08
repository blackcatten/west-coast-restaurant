from django.shortcuts import render
from django.views import generic, View
from .models import Guest_list, Reservations


class ReservationList(generic.ListView):
    model = Reservations
    template_name = "index.html"

