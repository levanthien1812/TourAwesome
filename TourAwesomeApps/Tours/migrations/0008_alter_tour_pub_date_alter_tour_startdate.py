# Generated by Django 4.1.3 on 2022-11-28 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0007_tour_ishot_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 28, 20, 5, 6, 997331)),
        ),
        migrations.AlterField(
            model_name='tour',
            name='startDate',
            field=models.DateField(),
        ),
    ]
