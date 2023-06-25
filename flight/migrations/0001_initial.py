# Generated by Django 4.2 on 2023-06-23 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=64)),
                ('airline', models.CharField(choices=[('THY', 'Turkish Airlines'), ('SUN', 'Sun Airlines'), ('PGS', 'Pegasus Airlines')], default='THY', max_length=3)),
                ('departure', models.PositiveSmallIntegerField(choices=[(1, 'Adana'), (6, 'Ankara'), (7, 'Antalya'), (9, 'Aydın'), (10, 'Balıkesir'), (16, 'Bursa'), (32, 'Isparta'), (34, 'Istanbul'), (35, 'Izmir'), (44, 'Malatya'), (52, 'Ordu')])),
                ('departure_date', models.DateField()),
                ('arrival', models.PositiveIntegerField(choices=[(1, 'Adana'), (6, 'Ankara'), (7, 'Antalya'), (9, 'Aydın'), (10, 'Balıkesir'), (16, 'Bursa'), (32, 'Isparta'), (34, 'Istanbul'), (35, 'Izmir'), (44, 'Malatya'), (52, 'Ordu')])),
                ('arrival_date', models.DateField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others'), ('P', 'Prefer Not to Say')], default='P', max_length=1)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ManyToManyField(to='flight.passenger')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]