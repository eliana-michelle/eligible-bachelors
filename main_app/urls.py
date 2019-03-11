from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),    
    path('bachelors/', views.bachelors_index, name = "index"),
    path('bachelors/<int:bachelor_id>/', views.bachelors_detail, name = "detail")
]