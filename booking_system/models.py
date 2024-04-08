from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


STATUS = ((0, "Draft"), (1, "Published"))


class Guest_list(models.Model):
    guest = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.guest)


class Reservations(models.Model):

    TIME_CHOICES = [
        ("12 PM - 2 PM", "12 PM - 2 PM"),
        ("1 PM - 3 PM", "1 PM - 3 PM"),
        ("2 PM - 4 PM", "2 PM - 4 PM"),
        ("3 PM - 5 PM", "3 PM - 5 PM"),
        ("4 PM - 6 PM", "4 PM - 6 PM"),
        ("5 PM - 7 PM", "5 PM - 7 PM"),
        ("6 PM - 8 PM", "6 PM - 8 PM"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservation'
    )
    full_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField()
    guest_list = models.ForeignKey(Guest_list, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.CharField(null=True, blank=False,
                            choices=TIME_CHOICES, max_length=60)

    def __str__(self):
        return str(self.date)

