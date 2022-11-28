from django.forms import ModelForm
from datetime import datetime
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
    startDate = forms.DateField(label='Nhập ngày bắt đầu')
    description = forms.CharField(
        label='Nhập mô tả của tour', min_length=10, max_length=1000, widget=forms.Textarea)
    highlight = forms.CharField(
        label='Mô tả những điểm nổi bật của tour', min_length=10, max_length=1000, widget=forms.Textarea)
    timeline = forms.FileField(
        label='Chọn file HTML hiển thị nội dung của lịch trình', required=False)
    isDomestic = forms.BooleanField(label='Trong nước?', required=False)
    duration_days = forms.IntegerField(label='Số ngày',min_value=0)
    duration_nights = forms.IntegerField(label='Số đêm',min_value=0)
    
    def clean_startDate(self):
        startDate = self.cleaned_data.get('startDate')
        if startDate < datetime.now():
            raise forms.ValidationError('Ngày khởi hành phải sau ngày hiện tại!')
        return startDate

    class Meta:
        model = Tour
        fields = ['id', 'name', 'location', 'price', 'startDate',
                  'description', 'highlight', 'isDomestic', 'timeline', 'duration_days', 'duration_nights']
        # fields = '__all__'
