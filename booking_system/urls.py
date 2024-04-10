from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationsList.as_view(), name='home'),
    path('make_reservation/', views.ReservationsDetail.as_view(), name='make_reservation'),
]