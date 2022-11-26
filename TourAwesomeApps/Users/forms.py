from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.EmailField(max_length=50)
    phoneNum = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    passwordConfirm = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username__iexact=username)
        if user.exists():
            raise forms.ValidationError(
                "Email này đã được dùng cho một tài khoản khác")
        return username

    def clean_passwordConfirm(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        if password != passwordConfirm:
            raise forms.ValidationError("Xác nhận mật khẩu không đúng")
        return passwordConfirm


class LoginForm(forms.Form):
    username = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user = User.objects.filter(username__iexact=username)
        if not user.exists():
            raise forms.ValidationError('Người dùng không tồn tại!')

        return username
