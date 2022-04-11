from django.contrib import admin
from .models import Reservation


# Register your models here.
# admin.site.register(Reservation)

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'room_id', 'start_date', 'end_date')
    search_fields = (
        'room_id', 'start_date', 'end_date')


admin.site.register(Reservation, ReservationAdmin)
