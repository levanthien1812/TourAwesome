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
    old_price = forms.FloatField(
        label='Nhập giá tiền gốc của tour', min_value=0)
    startDate = forms.DateField(
        label='Nhập ngày bắt đầu', widget=forms.SelectDateWidget)
    specialNote = forms.CharField(
        label='Nhập điểm đặc biệt', max_length=50)
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
        if startDate < datetime.now().date():
            raise forms.ValidationError('Ngày khởi hành phải sau ngày hiện tại!')
        return startDate
    
    def clean_old_price(self):
        old_price = self.cleaned_data.get(old_price)
        price = self.cleaned_data.get(price)
        if (old_price < price):
            raise forms.ValidationError('Gía khuyến mãi phải nhỏ hơn giá gốc!')
        return old_price

    class Meta:
        model = Tour
        fields = ['id', 'name', 'location', 'old_price', 'price', 'startDate', 'specialNote',
                  'description', 'highlight', 'isDomestic', 'timeline', 'duration_days', 'duration_nights']
        # fields = '__all__'
