from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
import uuid
import boto3

from .models import Bachelor, PriorFlame, Dealbreaker, Photo
from .forms import PriorFlameForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'eligiblebachelors'

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
    missing_dealbreakers = Dealbreaker.objects.exclude(id__in = bachelor.dealbreakers.all().values_list('id'))
    prior_flame_form = PriorFlameForm()
    return render(request, 'bachelors/details.html', {'bachelor': bachelor, 'prior_flame_form': prior_flame_form, 'dealbreakers': missing_dealbreakers})

def add_prior_flame(request, bachelor_id):
    form = PriorFlameForm(request.POST)
    if form.is_valid():
        new_old_flame = form.save(commit=False)
        new_old_flame.bachelor_id = bachelor_id
        new_old_flame.save()
    return redirect('detail', bachelor_id = bachelor_id)
    
class BachelorCreate(CreateView):
    model = Bachelor
    fields = '__all__'

class BachelorDelete(DeleteView):
    model = Bachelor
    success_url: '/bachelors/'

class BachelorUpdate(UpdateView):
    model = Bachelor
    fields = '__all__'

class DealbreakerList(ListView):
    model = Dealbreaker

class DealbreakerCreate(CreateView):
    model = Dealbreaker
    fields = '__all__'

class DealbreakerUpdate(UpdateView):
    model = Dealbreaker
    fields = ['content']

class DealbreakerDelete(DeleteView):
    model = Dealbreaker
    success_url = '/dealbreakers/'

def assoc_db(request, bachelor_id, dealbreaker_id):
    Bachelor.objects.get(id=bachelor_id).dealbreakers.add(dealbreaker_id)
    return redirect('detail', bachelor_id = bachelor_id)

def delete_db(request, bachelor_id, dealbreaker_id):
    Bachelor.objects.get(id=bachelor_id).dealbreakers.remove(dealbreaker_id)
    return redirect('detail', bachelor_id = bachelor_id)

def add_photo(request, bachelor_id):
	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, bachelor_id=bachelor_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', bachelor_id=bachelor_id)