from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationsList.as_view(), name='home'),
    path('reservations_detail/', views.ReservationsDetail.as_view(), name='reservations_detail'),
]