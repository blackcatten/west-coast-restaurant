from django import forms
from .models import Guest_list, Reservations


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = (
            'full_name', 'guest_list',
            'date', 'time',
            )