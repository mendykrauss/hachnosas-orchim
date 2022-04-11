from django.db import models
from hachnosas_orchim.users.models import Users


# Create your models here.
class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    total_occupancy = models.IntegerField()
    total_bedrooms = models.IntegerField()
    total_bathrooms = models.FloatField()
    room_description = models.TextField()
    has_kitchen = models.BooleanField()
    has_wifi = models.BooleanField()
    has_tv = models.BooleanField()
    has_air_conditioning = models.BooleanField()
    has_heating = models.BooleanField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'rooms'
        verbose_name_plural = 'Rooms'
        ordering = ['-published_date']
