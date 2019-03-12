from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),    
    path('bachelors/', views.bachelors_index, name = "index"),
    path('bachelors/<int:bachelor_id>/', views.bachelors_detail, name = "detail"),
    path('bachelors/create/', views.BachelorCreate.as_view(), name = "bachelors_create"),
    path('bachelors/<int:pk>/delete/', views.BachelorDelete.as_view(), name = "bachelor_delete"),
    path('bachelors/<int:pk>/update/', views.BachelorUpdate.as_view(), name = "bachelor_update" )
]