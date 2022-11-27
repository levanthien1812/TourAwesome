# Generated by Django 4.1.3 on 2022-11-27 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tours', '0003_alter_tourimage_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('bookingDate', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('tourID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours.tour')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
