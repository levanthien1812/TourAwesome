import random
import string
from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Tour, TourImage, TourVehicle, TourLocation
from TourAwesomeApps.Blogs.models import Blog
from TourAwesomeApps.Tours.forms import CreateTourForm
from TourAwesome.decorators import allowed_user, unauthenticated_user
from TourAwesomeApps.Blogs.views import getBlogs

def homeView(request):
    if not ('location' in request.GET):
        hotTours = getHotTours()
        domesticTours = getDomesticTour(True)
        foreignTours = getDomesticTour(False)
        blogs = getBlogs(request)
        tourLocations = getTourLocations()
        
        context = {
            'hotTours': hotTours,
            'domesticTours': domesticTours,
            'foreignTours': foreignTours,
            'blogs': blogs,
            'locations': tourLocations,
        }
        
        return render(request, 'home.html', context)

    else:
        location = request.GET['location']
        # print(location)
        locationTours = getToursByLocation(location)
        # print(locationTours)
        return render(request, 'Tours/search.html', {'tours': locationTours})
        
    

def showDomesticTours(request):
    domesticTours = getDomesticTour(True)
    if (domesticTours != None):
        return render(request, 'Tours/domestic-tours.html', {'tours': domesticTours})

def showForeignTours(request):
    foreignTours = getDomesticTour(False)
    if (foreignTours != None):
        return render(request, 'Tours/foreign-tours.html', {'tours': foreignTours})

def getDomesticTour(isDomestic):
    domesticTours = []
    tours = Tour.objects.filter(isDomestic = isDomestic) or None
    if tours != None:
        for tour in tours:
            image = TourImage.objects.filter(tour=tour).first()
            vehicles = TourVehicle.objects.filter(tour=tour)
            domesticTours.append({'tour': tour, 'image': image, 'vehicles': vehicles})
            
    return domesticTours

def getHotTours():
    hotTours = []
    tours = Tour.objects.all()[:8] or None
    if tours != None:
        for tour in tours:
            image = TourImage.objects.filter(tour=tour).first()
            vehicles = TourVehicle.objects.filter(tour=tour)
            if tour.pub_date.date() > datetime.now().date() - timedelta(days=10):
                tour.isHot = True
                hotTours.append({'tour': tour, 'image': image, 'vehicles': vehicles})
            else:
                tour.isHot = False
            tour.save()
            
    return hotTours
def getTourLocations():
    tourLcts = TourLocation.objects.filter(numTours__gte=1)[:10] or None
    return tourLcts

def getToursByLocation(location):
    tours = Tour.objects.filter(location__icontains = location) or None
    return tours

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
    lct = tour.location
    location = TourLocation.objects.filter(location=lct) or None
    
    if location != None:
        location.numTours += 1
        location.save()
    else:
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
        print(request.POST)
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
            
            return redirect(reverse('home'))
        
    return render(request, 'Tours/create.html', {'form': form, 'vehicles': vehicles_choices})

def getTour(request):
    return 

@login_required
@allowed_user(['admin'])
def updateTour(request, pk):
    tour = Tour.objects.get(id=pk) or None
    if tour == None:
        return Http404('Không tìm thấy tour này!')
    
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
            
            return redirect(reverse('home'))
        
    return render(request, 'Tours/create.html', {'form': form, 'vehicles': vehicles_choices})

@login_required
@allowed_user(['admin'])
def deleteTour(request, pk):
    tour = Tour.objects.get(id=pk) or None
    if tour == None:
        return Http404('Không tìm thấy tour này!')
    
    Tour.objects.filter(id=pk).delete()
    return redirect(reverse('home'))
    