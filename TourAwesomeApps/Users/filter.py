from django import forms
import django_filters
from django_filters import CharFilter, ChoiceFilter, DateFilter
from .models import *
from django.contrib.auth import get_user_model
from TourAwesomeApps.Tours.models import Tour

User = get_user_model()

is_staff_choices = (
    (True, 'Nhân viên'),
    (False, 'Người dùng')
)

class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Họ và tên')
    email = CharFilter(field_name='email', lookup_expr='icontains', label='Email')
    phoneNum = CharFilter(field_name='phoneNum', label='Số điện thoại')
    is_staff = ChoiceFilter(field_name='is_staff', label='Vai trò', choices=is_staff_choices)
    sex = ChoiceFilter(field_name='sex', label='Giới tính', choices=sex_choices)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'phoneNum', 'is_staff', 'sex']
        
        
isDomestic_choices = (
    (True, 'Trong nước'),
    (False, 'Ngoài nước')
)

class TourFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Tiêu đề tour')
    location = CharFilter(field_name='location', lookup_expr='icontains', label='Địa điểm')
    price_greater = CharFilter(field_name='price', lookup_expr='gte', label='Gía cao hơn')
    price_less = CharFilter(field_name='price', lookup_expr='lte', label='Gía thấp hơn')
    isDomestic = ChoiceFilter(field_name='isDomestic', label='Trong nước?', choices=isDomestic_choices)
    
    class Meta:
        model = Tour
        fields = ['name', 'location', 'price_greater', 'price_less', 'isDomestic']
        
class BookingFilter(django_filters.FilterSet):
    date_after = DateFilter(field_name='bookingDate', lookup_expr='gte',
                            label='Ngày đặt tour sau', widget=forms.DateInput(attrs={'type': 'date'}))
    date_before = DateFilter(field_name='bookingDate', lookup_expr='lte',
                             label='Ngày đặt tour trước', widget=forms.DateInput(attrs={'type': 'date'}))
    price_greater = CharFilter(field_name='price', lookup_expr='gte', label='Gía cao hơn')
    price_less = CharFilter(field_name='price', lookup_expr='lte', label='Gía thấp hơn')
    status = ChoiceFilter(field_name='status', label='Trạng thái', choices=status_choices)
    
    class Meta:
        model = Booking
        fields = ['date_after', 'date_before', 'price_greater', 'price_less', 'status']