import django_filters
from django_filters import CharFilter, ChoiceFilter, BooleanFilter
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
        
        
class TourFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Họ và tên')
    location = CharFilter(field_name='location', lookup_expr='icontains', label='Địa điểm')
    price_greater = CharFilter(field_name='price', lookup_expr='gte', label='Gía cao hơn')
    price_less = CharFilter(field_name='price', lookup_expr='lte', label='Gía thấp hơn')
    isDomestic = BooleanFilter(field_name='isDomestic', label='Trong nước?')
    
    class Meta:
        model = Tour
        fields = ['name', 'location', 'price_greater', 'price_less', 'isDomestic']