from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Bachelor: 
    def __init__(self, name, age, wealth_origin, net_worth, location, dealbreaker, image):
        self.name = name
        self.age = age
        self.wealth_origin = wealth_origin
        self.location = location
        self.net_worth = net_worth 
        self.dealbreaker = dealbreaker
        self.image = image
   
bachelors = [
    Bachelor("Louis Tomlinson", 27, "Former member of One Direction", 70000000, "UK", "Has a kid", 'http://images6.fanpop.com/image/photos/35200000/Louis-Tomlinson-louis-tomlinson-35269575-480-480.jpg'),
    Bachelor("Jack Schlossberg", 26, "JFK's Grandson", 100000000, "Boston, USA", "The Kennedys are known to die", 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/jackschlossberg-1513698574.jpg?crop=1xw:1xh;center,top&resize=480:*'),
    Bachelor("Timothee Chalamet", 22, "actor", 6000000, "New York City, USA", "Currently dating Johnny Depp's daughter", 'https://media.kitag.com/filer_public_thumbnails/filer_public/c6/40/c640f03c-0978-4af0-9c83-81b8e2b4a794/timothee_chalamet_kitagcinemas.jpg__492x729_q70.jpg'),
]

def bachelors_index(request):
    return render(request, 'bachelors/index.html', {'bachelors': bachelors})

