from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tour, TourImage
from TourAwesomeApps.Tours.forms import CreateTourForm
from TourAwesome.decorators import allowed_user, unauthenticated_user

def homeView(request):
    return render(request, 'home.html')

@login_required
@allowed_user(['admin'])
def createTour(request):
    form = CreateTourForm()

    if request.method == 'POST':
        form = CreateTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.isDomestic = form.cleaned_data['isDomestic']
            tour.save()
            
            images = request.FILES.getlist('images')
            for image in images:
                TourImage.objects.create(
                    tour = tour,
                    image = image
                )
            
            return HttpResponse('Tour created successfully!')
        else:
            raise Http404()

    return render(request, 'Tours/create.html', {'form': CreateTourForm})
