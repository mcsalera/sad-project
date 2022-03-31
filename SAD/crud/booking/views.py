from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing

def home(request):
    context = {
        'listings': Listing.objects.all()
    }
    return render(request, 'booking/home.html', context)

def about(request):
    return render(request, 'booking/about.html', {'title': 'About'})
# Create your views here.
