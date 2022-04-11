from django.contrib import admin
from .models import Rooms
# Register your models here.
# admin.site.register(Rooms)


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'room_type', 'total_occupancy', 'room_description')
    list_filter = ('room_name', 'room_type', 'total_occupancy', 'room_description')
    search_fields = ('room_name', 'room_type', 'total_occupancy', 'room_description')
    list_per_page = 10


admin.site.register(Rooms, RoomsAdmin)
