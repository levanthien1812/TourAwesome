from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def bookTour(request):
    user = request.user
    tourID = request.section.get('id') or None
