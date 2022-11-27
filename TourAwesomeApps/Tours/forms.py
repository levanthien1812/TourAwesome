from django.forms import ModelForm
from django import forms
from .models import Tour


class CreateTourForm(ModelForm):
    id = forms.CharField(label='Nhập ID của tour',
                         max_length=10)
    name = forms.CharField(label='Nhập tiêu đề tour',
                           max_length=200)
    location = forms.CharField(
        label='Nhập địa điểm tour', max_length=30)
    price = forms.FloatField(
        label='Nhập giá tiền của tour', min_value=0)
    startDate = forms.CharField(label='Nhập ngày bắt đầu', max_length=100)
    description = forms.CharField(
        label='Nhập mô tả của tour', max_length=1000, widget=forms.Textarea)
    highlight = forms.CharField(
        label='Mô tả những điểm nổi bật của tour', max_length=1000, widget=forms.Textarea)
    timeline = forms.FileField(
        label='Chọn file HTML hiển thị nội dung của lịch trình', required=False)
    isDomestic = forms.BooleanField(label='Trong nước?', required=False)
    duration_days = forms.IntegerField(label='Số ngày',min_value=0)
    duration_nights = forms.IntegerField(label='Số đêm',min_value=0)

    class Meta:
        model = Tour
        fields = ['id', 'name', 'location', 'price', 'startDate',
                  'description', 'highlight', 'isDomestic', 'timeline', 'duration_days', 'duration_nights']
        # fields = '__all__'
