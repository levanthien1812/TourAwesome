# Generated by Django 4.1.3 on 2022-11-30 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0004_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 17, 25, 14, 379641)),
        ),
    ]
