import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django.contrib.auth import get_user_model

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