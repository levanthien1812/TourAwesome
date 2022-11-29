# Generated by Django 4.1.3 on 2022-11-29 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0013_alter_tour_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='specialNote',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 10, 57, 9, 217608)),
        ),
    ]
