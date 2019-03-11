from django.shortcuts import render
from django.http import HttpResponse
from .models import Bachelor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bachelors_index(request):
    bachelors = Bachelor.objects.all().order_by('-net_worth')
    return render(request, 'bachelors/index.html', {'bachelors': bachelors})

def bachelors_detail(request, bachelor_id):
    bachelor = Bachelor.objects.get(id = bachelor_id)
    return render(request, 'bachelors/details.html', {'bachelor': bachelor})