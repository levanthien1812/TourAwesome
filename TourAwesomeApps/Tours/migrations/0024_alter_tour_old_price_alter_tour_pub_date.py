# Generated by Django 4.1.3 on 2022-12-08 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0023_alter_tour_price_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='old_price',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 19, 52, 26, 315962)),
        ),
    ]