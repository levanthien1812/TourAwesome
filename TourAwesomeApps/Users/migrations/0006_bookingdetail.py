# Generated by Django 4.1.3 on 2022-12-04 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_booking_startdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNum', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=150)),
                ('payment', models.CharField(choices=[('ATOFFICE', 'Thanh toán tại văn phòng'), ('BYTRANSFER', 'Chuyển khoản qua ngân hàng')], default=('ATOFFICE', 'Thanh toán tại văn phòng'), max_length=10)),
                ('bookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.booking')),
            ],
        ),
    ]
