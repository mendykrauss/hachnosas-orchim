# Generated by Django 4.0.3 on 2022-04-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_rooms_total_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_name',
            field=models.CharField(default='None for now', max_length=100),
            preserve_default=False,
        ),
    ]
