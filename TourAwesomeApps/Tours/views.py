from django.http import HttpResponse, Http404
from django.urls import reverse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Tour, TourImage, TourVehicle
from TourAwesomeApps.Blogs.models import Blog
from TourAwesomeApps.Tours.forms import CreateTourForm
from TourAwesome.decorators import allowed_user, unauthenticated_user
from TourAwesomeApps.Blogs.views import getBlogs

def homeView(request):
    hotTours = getHotTours()
    domesticTours = getDomesticTour(True)
    foreignTours = getDomesticTour(False)
    blogs = getBlogs(request)
    
    context = {
        'hotTours': hotTours,
        'domesticTours': domesticTours,
        'foreignTours': foreignTours,
        'blogs': blogs,
    }
    
    return render(request, 'home.html', context)

def showDomesticTours(request):
    domesticTours = getDomesticTour(True)
    if (domesticTours != None):
        return render(request, 'Tours/domestic-tours.html', {'tours': domesticTours})

def showForeignTours(request):
    foreignTours = getDomesticTour(False)
    if (foreignTours != None):
        return render(request, 'Tours/foreign-tours.html', {'tours': foreignTours})

def getDomesticTour(isDomestic):
    tours = Tour.objects.filter(isDomestic = isDomestic) or None
    return tours

def getHotTours():
    hotTours = []
    tours = Tour.objects.all() or None
    if tours != None:
        for tour in tours:
            if tour.pub_date.date() > datetime.now().date() - timedelta(days=10):
                tour.isHot = True
                hotTours.append(tour)
            else:
                tour.isHot = False
            tour.save()
            
    return hotTours

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
            
@login_required
@allowed_user(['admin'])
def createTour(request):
    form = CreateTourForm()
    vehicles_choices = TourVehicle.vehicles_choices

    if request.method == 'POST':
        form = CreateTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.isDomestic = form.cleaned_data['isDomestic']
            tour.pub_date = datetime.now()
            tour.save()
            
            createTourImage(request, tour)
            createTourVehicle(request, tour)
            
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
    