# Generated by Django 4.1.3 on 2022-12-04 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0012_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 1, 9, 12, 610060)),
        ),
    ]
