from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name = 'home'),
  path('destination_details', views.destination_details, name='destination_details'),
  path('travel_destination',views.travel_destination,name = 'travel_destination'),
  path('index',views.index,name = 'home'),
  path('contact',views.contact,name = 'contacts'),
  path('about',views.about,name = 'about'),
  path('elements',views.elements,name = 'elements')
  ]
