from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationsList.as_view(), name='home'),
    path(
        'make_reservation/',
        views.MakeReservations.as_view(),
        name='make_reservation'
    ),
    path(
        'reservations_detail/',
        views.ReservationsDetail.as_view(),
        name='reservations_detail'
    ),
    path(
        'update/<int:pk>/',
        views.UpdateReservation.as_view(),
        name='update_reservation'
    ),
    path(
        'delete/<int:pk>/',
        views.DeleteReservation.as_view(),
        name='delete_reservation'
    ),
]
