# Generated by Django 4.1.3 on 2022-12-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Đang đợi duyệt'), ('ACCEPTED', 'Đã duyệt')], max_length=10, null=True),
        ),
    ]
