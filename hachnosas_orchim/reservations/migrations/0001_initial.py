# Generated by Django 4.0.3 on 2022-04-11 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'db_table': 'reservations',
                'ordering': ['reservation_id'],
                'permissions': (('view_reservation', 'Can view reservation'), ('add_reservation', 'Can add reservation'), ('change_reservation', 'Can change reservation'), ('delete_reservation', 'Can delete reservation')),
                'abstract': False,
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AddIndex(
            model_name='reservation',
            index=models.Index(fields=['user_id'], name='reservation_user_id_a2c66d_idx'),
        ),
        migrations.AddIndex(
            model_name='reservation',
            index=models.Index(fields=['room_id'], name='reservation_room_id_c3c216_idx'),
        ),
        migrations.AddIndex(
            model_name='reservation',
            index=models.Index(fields=['start_date'], name='reservation_start_d_609f84_idx'),
        ),
        migrations.AddIndex(
            model_name='reservation',
            index=models.Index(fields=['end_date'], name='reservation_end_dat_107234_idx'),
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('user_id', 'room_id', 'start_date', 'end_date'), name='unique_reservation'),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('user_id', 'room_id', 'start_date', 'end_date')},
        ),
    ]
