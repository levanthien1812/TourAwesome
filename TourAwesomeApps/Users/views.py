from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from TourAwesomeApps.Users.forms import SignupForm, LoginForm, UpdateForm
from .models import sex_choices, Booking
from TourAwesomeApps.Tours.models import Tour
from TourAwesome.decorators import unauthenticated_user, allowed_user
from .filter import UserFilter, TourFilter

User = get_user_model()


@unauthenticated_user
def signup(request):
    signupForm = SignupForm()
    
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            name = signupForm.cleaned_data.get('name')
            email = signupForm.cleaned_data.get('email')
            phoneNum = signupForm.cleaned_data.get('phoneNum')
            password = signupForm.cleaned_data.get('password')
            passwordConfirm = signupForm.cleaned_data.get('passwordConfirm')
            
            # Auto generate username
            lastUser = User.objects.filter(username__startswith='user').last() or None
            if (lastUser != None):
                username = 'user{0}'.format(int(lastUser.username.replace('user', '')) + 1)
                print(username)
            else:
                username = 'user1'

            try:
                user = User.objects.create_user(username, email, password)
                print(user)
                user.phoneNum = phoneNum
                user.name = name
                
                group = Group.objects.get(name = 'customer')
                user.groups.add(group)
                
                user.save()
                
                messages.success(request, 'Tài khoản đã được tạo cho ' + email + '.Xin vui lòng đăng nhập!')
                return redirect(reverse('login'))
            except:
                user = None
                request.session['register_error'] = 1
        else:
            print('Form is invalid')
    
    loginForm = LoginForm()
    return render(request, 'Users/signinup.html', {'signupForm': signupForm, 'loginForm': loginForm})

@unauthenticated_user
def _login(request):
    loginForm = LoginForm()
    if (request.method == 'POST'):
        loginForm = LoginForm(request.POST)
        if (loginForm.is_valid()):
            email = loginForm.cleaned_data.get('email')
            password = loginForm.cleaned_data.get('password')
            
            try:
                _user = User.objects.filter(email=email).get()
                username = _user.username
                
                user = authenticate(request, username=username, password=password)
                #request.user = user
                login(request, user)
                messages.success(request, 'Chào mừng bạn trở lại')
                return redirect(reverse('home'))
            except:
                user = None
                messages.success(
                    request, 'Tên đăng nhập hoặc mật khẩu không đúng! Vui lòng thử lại.')
            
        else:
            print('Form is invalid')

    signupForm = SignupForm()
    return render(request, 'Users/signinup.html', {'loginForm': loginForm, 'signupForm': signupForm})

@login_required
def _logout(request):
    logout(request)
    return redirect('home')

@login_required
def update(request):
    user = User.objects.get(id=request.user.id)
    form = UpdateForm(instance=user)
    
    if (request.method == 'POST'):
        form = UpdateForm(request.POST, request.FILES, instance=user)
        print(request.POST)
        # print(form.changed_data)
        
        if form.is_valid():
            user = form.save(commit=False)
            newPassword = form.cleaned_data.get('newPassword')
            if (newPassword != ''):
                user.set_password(newPassword)
            user.save()
            
            messages.success(request, 'Cập nhật thông tin thành công')
            return redirect(reverse('update-account'))
        
        else:
            print('Form is invalid!')
        
    return render(request, 'Users/account.html', {'form': form, 'sex_choices': sex_choices})

@login_required
def showBookings(request):
    userID = request.user.id
    bookings = Booking.objects.filter(userID=userID) or None
    if bookings is None:
        print('You have no bookings to display!')
        
    return render(request, 'Users/bookings.html', {'bookings': bookings})

@login_required
@allowed_user(['admin'])
def manageUser(request):
    users = User.objects.all() or None
    
    staffs_count = User.objects.filter(is_staff=True).count
    users_count = User.objects.filter(is_staff=False, is_superuser=False).count
    
    userFilter = UserFilter(request.GET, queryset=users)
    users = userFilter.qs
    
    context = {
        'users': users,
        'staffs_count': staffs_count,
        'users_count': users_count,
        'userFilter': userFilter,
    }
    return render(request, 'Users/manage-user.html', context)


@login_required
@allowed_user(['admin'])
def deleteUser(request, pk):
    try:
        user = User.objects.filter(id=pk)
        print(pk)
        user.delete()
        
        messages.success(request, 'Xóa người dùng thành công')
        return redirect(reverse('manage-users'))
    except:
        user = None
        return render(request, 'Components/404page.html')
    

@login_required
@allowed_user(['admin'])
def manageTour(request):
    tours = Tour.objects.all() or None
    
    tourFilter = TourFilter(request.GET, queryset=tours)
    tours = tourFilter.qs

    context = {
        'tours': tours,
        'tourFilter': tourFilter
    }
    return render(request, 'Users/manage-tour.html', context)
