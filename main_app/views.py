from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

@login_required
def bachelors_index(request):
    bachelors = Bachelor.objects.filter(user = request.user).order_by('-net_worth')
    return render(request, 'bachelors/index.html', {'bachelors': bachelors})

@login_required
def bachelors_detail(request, bachelor_id):
    bachelor = Bachelor.objects.get(id = bachelor_id)
    missing_dealbreakers = Dealbreaker.objects.exclude(id__in = bachelor.dealbreakers.all().values_list('id'))
    prior_flame_form = PriorFlameForm()
    return render(request, 'bachelors/details.html', {'bachelor': bachelor, 'prior_flame_form': prior_flame_form, 'dealbreakers': missing_dealbreakers})

@login_required
def add_prior_flame(request, bachelor_id):
    form = PriorFlameForm(request.POST)
    if form.is_valid():
        new_old_flame = form.save(commit=False)
        new_old_flame.bachelor_id = bachelor_id
        new_old_flame.save()
    return redirect('detail', bachelor_id = bachelor_id)
    
class BachelorCreate(LoginRequiredMixin, CreateView):
    model = Bachelor
    fields = '__all__'

    def form_valid(self, form):
    # Assign the logged in user
        form.instance.user = self.request.user
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class BachelorDelete(LoginRequiredMixin, DeleteView):
    model = Bachelor
    success_url: '/bachelors/'

class BachelorUpdate(LoginRequiredMixin, UpdateView):
    model = Bachelor
    fields = '__all__'

class DealbreakerList(LoginRequiredMixin, ListView):
    model = Dealbreaker

class DealbreakerCreate(LoginRequiredMixin, CreateView):
    model = Dealbreaker
    fields = '__all__'

class DealbreakerUpdate(LoginRequiredMixin, UpdateView):
    model = Dealbreaker
    fields = ['content']

class DealbreakerDelete(LoginRequiredMixin, DeleteView):
    model = Dealbreaker
    success_url = '/dealbreakers/'

@login_required
def assoc_db(request, bachelor_id, dealbreaker_id):
    Bachelor.objects.get(id=bachelor_id).dealbreakers.add(dealbreaker_id)
    return redirect('detail', bachelor_id = bachelor_id)

@login_required
def delete_db(request, bachelor_id, dealbreaker_id):
    Bachelor.objects.get(id=bachelor_id).dealbreakers.remove(dealbreaker_id)
    return redirect('detail', bachelor_id = bachelor_id)

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)