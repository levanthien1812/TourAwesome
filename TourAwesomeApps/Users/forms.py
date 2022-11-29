from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.Form):
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
    
class UpdateForm(forms.Form):
    name = forms.EmailField(max_length=50)
    phoneNum = forms.CharField(max_length=11)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    passwordConfirm = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        user = User.objects.filter(name__iexact=name)
        if user.exists():
            raise forms.ValidationError(
                "Email này đã được dùng cho một tài khoản khác")
        return name

    def clean_passwordConfirm(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        if password != passwordConfirm:
            raise forms.ValidationError("Xác nhận mật khẩu không đúng")
        return passwordConfirm


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        user = User.objects.filter(email__iexact=email)
        if not user.exists():
            raise forms.ValidationError('Người dùng không tồn tại!')

        return email
