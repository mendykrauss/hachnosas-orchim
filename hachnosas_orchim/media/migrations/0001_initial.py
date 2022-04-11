# Generated by Django 4.0.3 on 2022-04-11 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media_Type',
            fields=[
                ('media_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('mime_type', models.CharField(max_length=255, null=True)),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.media_type')),
            ],
        ),
    ]