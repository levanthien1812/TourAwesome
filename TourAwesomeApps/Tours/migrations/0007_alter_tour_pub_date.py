# Generated by Django 4.1.3 on 2022-11-30 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0006_tour_old_price_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 2, 16, 15, 190048)),
        ),
    ]