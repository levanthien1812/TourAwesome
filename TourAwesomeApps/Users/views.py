from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout, get_user_model

from TourAwesomeApps.Users.forms import SignupForm, LoginForm

User = get_user_model()

def signup(request):
    form = SignupForm()

    if (request.method == 'POST'):
        form = SignupForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            phoneNum = form.cleaned_data.get('phoneNum')
            password = form.cleaned_data.get('password')
            passwordConfirm = form.cleaned_data.get('passwordConfirm')
            
            try:
                user = User.objects.create_user(username, username, password)
                user.phoneNum = phoneNum
                user.save()
            except:
                user = None
            if (user != None):
                login(request, user)
                return redirect(reverse('home'))
            else:
                request.session['register_error'] = 1
            
    return render(request, 'Users/signup.html', {'form': form})

def _login(request):
    form = LoginForm()
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user != None:
                #request.user = user
                login(request, user)
                return redirect(reverse('home'))
            else:
                request.section['invalid_user'] = 1
        else:
            print('Form is invalid')

    return render(request, 'Users/login.html', {'form': form})

def _logout(request):
    logout(request)
    return redirect('home')