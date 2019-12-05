from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Squirrel_Census
from .forms import SightingForm

def index(request):
    return HttpResponse("Hello, I am working on the Squirrel Tracker project.")

def map(request):
    sightings = Squirrel_Census.objects.all()
    context = {'sightings':sightings}
    return render(request,'SquirrelTracker/map.html',context)

def sightings(request):
    return HttpResponse("This page is reserved for the sightings list page.")

def update(request,squirrel_census_id):
    sighting = Squirrel_Census.objects.get(id=squirrel_census_id)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'sightings/{squirrel_census_id}')
    else:
        form = SightingForm(instance=sighting)

    context = {
            'form': form,
    }

    return render(request, 'SquirrelTracker/update.html', context)

def add_sightings(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingForm()

    context = {
            'form' : form,
            'jazz' : True,
    }

    return render(request, 'SquirrelTracker/update.html', context)

def stats(request):
    return HttpResponse("This page is reserved for presenting stats.")
