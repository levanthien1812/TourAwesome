from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from TourAwesomeApps.Users.forms import SignupForm, LoginForm
from TourAwesome.decorators import unauthenticated_user, allowed_user

User = get_user_model()


@unauthenticated_user
def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phoneNum = form.cleaned_data.get('phoneNum')
            password = form.cleaned_data.get('password')
            passwordConfirm = form.cleaned_data.get('passwordConfirm')
            
            userCount = User.objects.all().count()
            username = 'user{0}'.format(userCount)

            try:
                user = User.objects.create_user(username, email, password)
                print(user)
                user.phoneNum = phoneNum
                user.name = name
                
                # group = Group.objects.get(name = 'customer')
                # user.groups.add(group)
                
                user.save()
                
                messages.success(request, 'Tài khoản đã được tạo cho ' + email + '.Xin vui lòng đăng nhập!')
                return redirect(reverse('login'))
            except:
                print('Something went wrong')
                user = None
                request.session['register_error'] = 1
        else:
            print('Form is invalid')
            
    return render(request, 'Users/signup.html', {'form': form})

@unauthenticated_user
def _login(request):
    form = LoginForm()
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if (form.is_valid()):
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            username = User.objects.filter(email=email).get().username

            user = authenticate(request, username=username, password=password)

            if user != None:
                #request.user = user
                login(request, user)
                return redirect(reverse('home'))
            
        else:
            print('Form is invalid')

    return render(request, 'Users/login.html', {'form': form})

@login_required
def _logout(request):
    logout(request)
    return redirect('home')

def showAccount(request):
    
    return render(request, 'Users/account.html')

def showBookings(request):
    
    return render(request, 'Users/bookings.html')