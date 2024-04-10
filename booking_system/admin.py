from django.contrib import admin
from .models import Guest_list, Reservations

class Guest_listAdmin(admin.ModelAdmin):
    list_display = ('guest',)


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('full_name',
                    'guest_list', 'date')
    list_filter = ('date',)
    search_fields = ('full_name',)
    date_hierarchy = 'reservation_date'

admin.site.register(Guest_list)
admin.site.register(Reservations)
