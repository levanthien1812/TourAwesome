# Generated by Django 4.1.3 on 2022-12-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_bookingdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]