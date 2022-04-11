from django.db import models
from hachnosas_orchim.users.models import Users
from hachnosas_orchim.rooms.models import Rooms
# Create your models here.


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.reservation_id)

    class Meta:
        db_table = 'reservations'
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ['reservation_id']
        unique_together = ('user_id', 'room_id', 'start_date', 'end_date')
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['room_id']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'room_id', 'start_date', 'end_date'], name='unique_reservation'),
        ]
        default_permissions = ()
        permissions = (
            ('view_reservation', 'Can view reservation'),
            ('add_reservation', 'Can add reservation'),
            ('change_reservation', 'Can change reservation'),
            ('delete_reservation', 'Can delete reservation'),
        )
        app_label = 'reservations'
        abstract = False
        managed = True