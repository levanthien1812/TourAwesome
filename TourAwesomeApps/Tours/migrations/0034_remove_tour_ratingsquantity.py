# Generated by Django 4.1.3 on 2022-12-23 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0033_alter_tour_ratingsquantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='ratingsQuantity',
        ),
    ]
