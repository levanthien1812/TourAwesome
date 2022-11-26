from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Tour, TourImage
from TourAwesomeApps.Tours.forms import CreateTourForm
from django.http import HttpResponse
from django.shortcuts import render


def homeView(request):
    return render(request, 'home.html')

@login_required
def createTour(request):
    form = CreateTourForm()

    if request.method == 'POST':
        form = CreateTourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.isDomestic = form.cleaned_data['isDomestic']
            tour.save()
            return HttpResponse('Tour created successfully!')
        else:
            print('Form is not valid!')

    return render(request, 'Tours/create.html', {'form': CreateTourForm})
