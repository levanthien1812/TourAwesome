from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .filter import UserFilter

from TourAwesomeApps.Users.forms import SignupForm, LoginForm, UpdateForm
from .models import sex_choices, Booking
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
                raise Http404('Something went wrong')
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
                messages.success(request, 'Chào mừng bạn trở lại')
                return redirect(reverse('home'))
            
        else:
            print('Form is invalid')

    return render(request, 'Users/login.html', {'form': form})

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
    user = User.objects.filter(id=pk) or None
    if (user == None):
        raise Http404('User not found!')
    user.delete()
    
    messages.success(request, 'Xóa người dùng thành công')
    return redirect(reverse('manage-users'))