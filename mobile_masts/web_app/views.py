from django.http import HttpResponse
from django.shortcuts import render
from .models import Property

def index(request):
    all_property = Property.objects.all()
    return render(request, 'stats/index.html', {'all_property': all_property})

def create(request):
    return render(request, 'stats/create.html')
