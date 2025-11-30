from django.shortcuts import render
from .models import Destination , Place
# Create your views here.
def index(request):
  
  dests = Destination.objects.all()
  places = Place.objects.all()
  return render(request,"index.html",{'dests' : dests,'places' : places})

def destination_details(request):
  return render(request,"destination_details.html")

def travel_destination(request):
  return render(request,"travel_destination.html")
def contact(request):
  return render(request,"contact.html")
def about(request):
  return render(request,"about.html")
def elements(request):
  return render(request,"elements.html")