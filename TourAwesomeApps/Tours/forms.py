from django.forms import ModelForm
from datetime import datetime
from django import forms
from .models import Tour


class CreateTourForm(ModelForm):
    name = forms.CharField(label='Nhập tiêu đề tour', max_length=200)
    location = forms.CharField(max_length=30)
    detailLocation = forms.CharField(max_length=50)
    price = forms.FloatField(min_value=0)
    old_price = forms.FloatField(min_value=0)
    startDate = forms.DateField(widget=forms.SelectDateWidget)
    specialNote = forms.CharField(max_length=50)
    description = forms.CharField(min_length=10, max_length=1000, widget=forms.Textarea)
    highlight = forms.CharField(min_length=10, max_length=1000, widget=forms.Textarea)
    timeline = forms.FileField(required=False)
    isDomestic = forms.BooleanField(required=False)
    duration_days = forms.IntegerField(min_value=0)
    duration_nights = forms.IntegerField(min_value=0)
    
    def clean_startDate(self):
        startDate = self.cleaned_data.get('startDate')
        if startDate < datetime.now().date():
            raise forms.ValidationError('Ngày khởi hành phải sau ngày hiện tại!')
        return startDate
    
    def clean_price(self):
        old_price = self.cleaned_data.get('old_price')
        price = self.cleaned_data.get('price')
        if old_price < price:
            raise forms.ValidationError('Gía khuyến mãi phải nhỏ hơn giá gốc!')
        return price

    class Meta:
        model = Tour
        fields = ['name', 'location', 'detailLocation', 'old_price', 'price', 'startDate', 'specialNote',
                  'description', 'highlight', 'isDomestic', 'timeline', 'duration_days', 'duration_nights']
        # fields = '__all__'
