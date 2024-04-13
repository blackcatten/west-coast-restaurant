from django import forms
from .models import Guest_list, Reservations
from datetime import date, timedelta


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = (
            'full_name', 'guest_list',
            'date', 'time',
            )
        exclude = ["user"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    def get_available_dates(self):
        booked_dates = Reservations.objects.values_list('date', flat=True)

        today = date.today()
        end_date = today + timedelta(days=30)
        available_dates = [
            today + timedelta(days=i)
            for i in range((end_date - today).days)
        ]

        available_dates = [
            date for date in available_dates if date not in booked_dates
        ]

        return available_dates