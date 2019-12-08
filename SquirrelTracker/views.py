from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Squirrel_Census
from .forms import SightingForm

from django.db.models import Count

# Create your views here.
def index(request):
    return HttpResponse("Hello, I am working on the Squirrel Tracker project.")

def sightings(request):
    if request.method == 'GET':
        context = {}
        context['title'] ="Total Item List"
        fields = ('id','latitude','longitude','unique_squirrel_id','shift','date','age','primary_fur_color','location',
            'specific_location','running','chasing','climbing','eating','foraging','other_activities','kuks',
            'quaas','moans','tail_flags','tail_twitches','approaches','indifferent','runs_from')
        context['fields'] = fields
        context['Squirrel_Census_list'] =  Squirrel_Census.objects.all()
        return render(request,'list.html',context)

    #return HttpResponse("This page is reserved for the sightings list page.")

def map(request):
    sightings = Squirrel_Census.objects.all()
    context = {'sightings':sightings}
    return render(request,'map.html',context)

def update(request,squirrel_census_id):
    sighting = Squirrel_Census.objects.get(id=squirrel_census_id)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/SquirrelTracker/sightings/{squirrel_census_id}')
    else:
        form = SightingForm(instance=sighting)

    context = {
            'form': form,
    }

    return render(request, 'update.html', context)

def add_sightings(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/SquirrelTracker/sightings/')
    else:
        form = SightingForm()

    context = {
            'form' : form,
            'jazz' : True,
    }

    return render(request, 'update.html', context)

def stats(request):
    if request.method == 'GET':
        context = {}
        context['title'] ="Stats by item properties"
        fields = ('shift','age','primary_fur_color','location',
            'running','chasing','climbing','eating','foraging','kuks',
            'quaas','moans','tail_flags','tail_twitches','approaches','indifferent','runs_from')
        stats_content={}
        for field in fields:
            key = field
            stats_content[key] = Squirrel_Census.objects.extra(
                select = {
                    'property': key
                }
            ).values('property').annotate(dcount=Count(key))
            print(key,len(stats_content[key]), stats_content[key])

        context['stats_content'] = stats_content

        return render(request,'stats.html',context)
    #return HttpResponse("This page is reserved for presenting stats.")