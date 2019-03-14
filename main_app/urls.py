from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),    
    path('bachelors/', views.bachelors_index, name = "index"),
    path('bachelors/<int:bachelor_id>/', views.bachelors_detail, name = "detail"),
    path('bachelors/create/', views.BachelorCreate.as_view(), name = "bachelors_create"),
    path('bachelors/<int:pk>/delete/', views.BachelorDelete.as_view(), name = "bachelor_delete"),
    path('bachelors/<int:pk>/update/', views.BachelorUpdate.as_view(), name = "bachelor_update" ),
    path('bachelors/<int:bachelor_id>/add_prior_flame/', views.add_prior_flame, name = "add_prior_flame"),
    path('dealbreakers/', views.DealbreakerList.as_view(), name = "dealbreakers_index"),
    path('dealbreakers/create/', views.DealbreakerCreate.as_view(), name = "dealbreaker_create"),
    path('dealbreakers/<int:pk>/update/', views.DealbreakerUpdate.as_view(), name = "dealbreaker_update"),
    path('dealbreakers/<int:pk>/delete/', views.DealbreakerDelete.as_view(), name = "dealbreaker_delete"),
    path('bachelors/<int:bachelor_id>/assoc_db/<int:dealbreaker_id>/', views.assoc_db, name='assoc_db'),
    path('bachelors/<int:bachelor_id>/delete_db/<int:dealbreaker_id>/', views.delete_db, name='delete_db'), 
    path('bachelors/<int:bachelor_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]