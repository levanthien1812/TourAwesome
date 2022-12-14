from django import forms
from django.contrib.auth import get_user_model
from .models import sex_choices, payment_choices, Booking, BookingDetail

User = get_user_model()

class SignupForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phoneNum = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    passwordConfirm = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email)
        if user.exists():
            raise forms.ValidationError(
                "Email này đã được dùng cho một tài khoản khác")
        return email

    def clean_passwordConfirm(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        if password != passwordConfirm:
            raise forms.ValidationError("Xác nhận mật khẩu không đúng")
        return passwordConfirm
    
    class Meta:
        model = User
        fields = ['name', 'email', 'phoneNum', 'password']
    
class UpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False)
    phoneNum = forms.CharField(max_length=11, required=False)
    email = forms.EmailField(required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id': 'image'
    }), required=False)
    birthday = forms.DateField(widget=forms.SelectDateWidget, required=False)
    sex = forms.ChoiceField(required=False, choices=sex_choices, widget=forms.RadioSelect)
    # password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=False)
    # newPassword = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            user = User.objects.filter(email__iexact=email)
            if user.exists():
                raise forms.ValidationError(
                    "Email này đã được dùng cho một tài khoản khác")
                
        return email
    
    class Meta:
        model = User
        fields = ['image', 'name', 'birthday', 'sex', 'email', 'phoneNum']

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')

    #     user = User.objects.filter(email__iexact=email)
    #     if not user.exists():
    #         raise forms.ValidationError('Người dùng không tồn tại!')

    #     return email
    
class BookingDetailForm (forms.ModelForm):
    name = forms.CharField(max_length=30, widget=forms.TextInput)
    email = forms.EmailField()
    phoneNum = forms.CharField(max_length=11)
    address = forms.CharField(max_length=150)
    payment = forms.ChoiceField(choices=payment_choices, widget=forms.RadioSelect)
    
    class Meta:
        model = BookingDetail
        fields = ['name', 'email', 'phoneNum', 'address', 'payment']
        
