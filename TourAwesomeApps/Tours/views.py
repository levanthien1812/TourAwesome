import random
import string
from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import F, Q

from .models import *
from TourAwesomeApps.Users.models import Booking
from TourAwesomeApps.Blogs.models import Blog
from TourAwesomeApps.Tours.forms import CreateTourForm
from TourAwesomeApps.Users.forms import BookingDetailForm
from TourAwesome.decorators import allowed_user, unauthenticated_user

User = get_user_model()

def homeView(request):
    updateHotTours()
    
    tours = toursWithImages(Tour.objects.all()[:20])
    hotTours = getHotTours()
    tourLocations = getTourLocations()
    blogs = Blog.objects.all()[:6]
    
    
    if not ('location' in request.GET):
        context = {
            'hotTours': hotTours,
            'tours': tours,
            'blogs': blogs,
            'locations': tourLocations,
        }
        
        return render(request, 'Tours/home.html', context)

    else:
        location = request.GET['location']
        # print(location)
        locationTours = getToursByLocation(location)
        # print(locationTours)
        context = {
            'tours': locationTours,
            'location': location,
            'blogs': blogs,
            'locations': tourLocations,
        }
        return render(request, 'Tours/search.html', context)
        
def toursWithImages(tours):
    toursWithImages = []
    if tours != None:
        for tour in tours:
            image = TourImage.objects.filter(tour=tour).first()
            vehicles = TourVehicle.objects.filter(tour=tour)
            toursWithImages.append(
                {'tour': tour, 'image': image, 'vehicles': vehicles})
    return toursWithImages
    
def getHotTours():
    tours = Tour.objects.all().order_by('-bookingCount')
    tours = toursWithImages(tours)
    return tours

def updateHotTours():
    tours = Tour.objects.all()
    if tours != None:
        for tour in tours:
            if tour.pub_date.date() > datetime.now().date() - timedelta(days=10):
                tour.isHot = True
            else:
                tour.isHot = False
            tour.save()
            
def getTourLocations():
    tourLcts = TourLocation.objects.filter(numTours__gte=1).order_by('-numTours')[:10] or None
    return tourLcts

def getToursByLocation(location):
    tours = Tour.objects.filter(Q(location__icontains=location) | Q(detailLocation__icontains=location)) or None
    return toursWithImages(tours)

def deleteTourImage(tour):
    TourImage.objects.filter(tour=tour).delete()

def createTourImage(request, tour):
    images = request.FILES.getlist('images') or None
    if (images != None):
        if 'update' in request.path:
            deleteTourImage(tour)
            
        for image in images:
            TourImage.objects.create(
                tour=tour,
                image=image
            )
        
def deleteTourVehicle(tour):
    TourVehicle.objects.filter(tour=tour).delete()
    
def createTourVehicle(request, tour):
    vehicles_choices = TourVehicle.vehicles_choices
    if 'update' in request.path:
        for vehicle in vehicles_choices:
            if request.POST.get(vehicle[0], False): 
                deleteTourVehicle(tour=tour)
                break
    for vehicle in vehicles_choices:
        if request.POST.get(vehicle[0], False):
            TourVehicle.objects.create(
                tour=tour,
                vehicle=vehicle[0]
            )
            
def updateLocationModel(tour):
    lcts = tour.location
    lctArr = lcts.split(' - ')
    print(lctArr)
    for lct in lctArr:
        try:
            location = TourLocation.objects.filter(location=lct).get()
            numTours = location.numTours + 1
            TourLocation.objects.filter(location=lct).update(numTours=numTours)
        except:
            TourLocation.objects.create(
                location=lct,
                numTours=1
            )
            
@login_required
@allowed_user(['admin'])
def createTour(request):
    form = CreateTourForm()
    vehicles_choices = TourVehicle.vehicles_choices

    if request.method == 'POST':
        form = CreateTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            
            # generate random ID    
            first_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
            second_part = ''.join(random.choice(string.digits) for _ in range(5))
            id = first_part + second_part
            tour.id = id
            
            tour.isDomestic = form.cleaned_data['isDomestic']
            tour.pub_date = datetime.now()
            tour.save()
            
            createTourImage(request, tour)
            createTourVehicle(request, tour)
            updateLocationModel(tour)
            
            messages.success(request, 'Tạo tour thành công!')
            return redirect(reverse('manage-tours'))
        
    return render(request, 'Tours/create.html', {'form': form, 'vehicles': vehicles_choices})

# def detailCheckLogin(request, pk):
#     if request.user:
#         return render(request, 'Components/not-allow.html')
    
#     getTour(request, pk)

def getTour(request, pk):
    # try:
        tour = Tour.objects.get(id=pk)
        images = TourImage.objects.filter(tour=tour)
        vehicles = TourVehicle.objects.filter(tour=tour)
        reviews = Review.objects.filter(tour=tour) or None
        
        timeline_file = open(
            'media/{0}'.format(tour.timeline), 'r', encoding="utf8")
        timeline = timeline_file.read()
        
        bookingDetailForm = BookingDetailForm(initial={
            'name': request.user.name,
            'email': request.user.email,
            'phoneNum': request.user.phoneNum,
        })
        
        context = {
            'tour': tour,
            'images': images,
            'vehicles': vehicles,
            'timeline': timeline,
            'bookingDetailForm': bookingDetailForm,
            'reviews': reviews,
            'locations': getTourLocations(),
        }
        return render(request, 'Tours/detail.html', context)
    # except:
    #     tour = None
    #     return render(request, 'Components/404page.html')

@login_required
@allowed_user(['admin'])
def updateTour(request, pk):
    try:
        tour = Tour.objects.get(id=pk)
        
        form = CreateTourForm(instance=tour)
        vehicles_choices = TourVehicle.vehicles_choices

        if request.method == 'POST':
            form = CreateTourForm(request.POST, request.FILES, instance=tour)
            if form.is_valid():
                updateTour = form.save(commit=False)
                updateTour.isDomestic = form.cleaned_data['isDomestic']
                updateTour.pub_date = datetime.now()
                updateTour.save()
                
                createTourImage(request, tour)
                createTourVehicle(request, tour)
                
                messages.success(request, 'Cập nhật tour thành công')
                return redirect(reverse('home'))
            
        return render(request, 'Tours/create.html', {'form': form, 'vehicles': vehicles_choices})
    except:
        tour = None
        return render(request, 'Components/404page.html')

@login_required
@allowed_user(['admin'])
def deleteTour(request, pk):
    # try:
    tour = Tour.objects.filter(id=pk).get()
    lcts = tour.location.split(' - ')
    for lct in lcts:
        tourLct = TourLocation.objects.filter(location=lct).get()
        
        if tourLct.numTours > 1:
            numTours = tourLct.numTours - 1
            TourLocation.objects.filter(location=lct).update(numTours=numTours)
        else:
            TourLocation.objects.filter(location=lct).delete()
            
    Tour.objects.filter(id=pk).delete()
        
    messages.success(request, 'Xóa tour thành công')
    return redirect(reverse('manage-tours'))
    # except:
    #     tour = None
    #     return render(request, 'Components/404page.html')
    
@login_required
@allowed_user(['customer'])
def bookTour(request, pk):
    bookingDetailForm = BookingDetailForm()
    
    if request.method == 'POST':
        try:
            tour = Tour.objects.get(id=pk)
            user = User.objects.get(id=request.user.id)
            
            bookingObj = {
                'tourID': tour,
                'userID': user,
                'startDate': request.POST.get('startDate'),
                'quantity': request.POST.get('quantity'),
                'price': request.POST.get('price'),
                'bookingDate': datetime.now().date()
            }
            
            booking = Booking.objects.create(**bookingObj) or None
            
            bookingDetailForm = BookingDetailForm(request.POST)
            bookingDetail = bookingDetailForm.save(commit=False)
            if bookingDetail.bookingID_id == None:
                bookingDetail.bookingID_id = booking.id
            bookingDetail.save()
            Tour.objects.filter(id=pk).update(bookingCount=F('bookingCount')+1)
            
            if booking:
                messages.success(request, 'Bạn đã đặt tour thành công! Đơn đặt tour của bạn sẽ được duyệt sớm nhất có thể!')
                return redirect(reverse('home'))
            else:
                return Http404('Something went wrong')
        except:
            tour = None
            return render(request, 'Components/404page.html')


def introduce(request):
    return render(request, 'Tours/introduce.html')

def addReview(request, pk):
    try:
        tour = Tour.objects.get(id=pk)
        user = request.user
        
        newReview = {
            'tour': tour,
            'user': user,
            'content': request.POST['content'],
        }
        
        Review.objects.create(**newReview)
        
        return redirect(reverse('get-tour', args=[tour.id]))
    except:
        tour = None
        return render(request, 'Components/404page.html')
