# Generated by Django 4.1.3 on 2022-12-08 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0022_alter_tour_pub_date_alter_tourlocation_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 19, 51, 26, 997450)),
        ),
    ]