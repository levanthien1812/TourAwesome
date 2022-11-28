from django.urls import reverse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

from .models import Tour, TourImage, TourVehicle
from TourAwesomeApps.Blogs.models import Blog
from TourAwesomeApps.Tours.forms import CreateTourForm
from TourAwesome.decorators import allowed_user, unauthenticated_user

def homeView(request):
    hotTours = getHotTours()
    domesticTours = getDomesticTour(True)
    foreignTours = getDomesticTour(False)
    
    context = {
        'hotTours': hotTours,
        'domesticTours': domesticTours,
        'foreignTours': foreignTours
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
                tour.isHot = False
                hotTours.append(tour)
            
    return hotTours

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
            
            images = request.FILES.getlist('images')
            for image in images:
                TourImage.objects.create(
                    tour = tour,
                    image = image
                )

            for vehicle in vehicles_choices:
                if request.POST.get(vehicle[0], False):
                    TourVehicle.objects.create(
                        tour = tour,
                        vehicle = vehicle[0]
                    )
            
            return redirect(reverse('home'))
        else:
            print('Form is invalid!')
            raise Http404()
        
    return render(request, 'Tours/create.html', {'form': form, 'vehicles': vehicles_choices})

