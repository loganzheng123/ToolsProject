from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel_Census

def index(request):
    return HttpResponse("Hello, I am working on the Squirrel Tracker project.")

def map(request):
    sightings = Squirrel_Census.objects.all()
    context = {'sightings':sightings}
    return render(request,'SquirrelTracker/map.html',context)

def sightings(request):
    return HttpResponse("This page is reserved for the sightings list page.")

def update(request,squirrel_census_id):
    response = "This page is reserved for the update and delete of the %s sightings."
    return HttpResponse(response % squirrel_census_id)

def add_sightings(request):
    return HttpResponse("This page is reserved for adding sightings.")

def stats(request):
    return HttpResponse("This page is reserved for presenting stats.")
