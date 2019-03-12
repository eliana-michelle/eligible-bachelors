from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

class BachelorCreate(CreateView):
    model = Bachelor
    fields = '__all__'

class BachelorDelete(DeleteView):
    model = Bachelor
    success_url: '/bachelors/'

class BachelorUpdate(UpdateView):
    model = Bachelor
    fields = '__all__'