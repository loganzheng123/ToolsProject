from django.urls import path

from . import views

urlpatterns = [
    #ex: /SquirrelTracker/
    path('', views.index, name='index'),
    #ex: /SquirrelTracker/sightings/
    path('sightings/', views.sightings, name='sightings'),
    #ex: /SquirrelTracker/sightings/map
    path('sightings/map', views.map, name='map'),
    #ex: /SquirrelTracker/sightings/5/
    path('sightings/<int:squirrel_census_id>/', views.update, name='update'),
    #ex: /SquirrelTracker/sightings/add/
    path('sightings/add/', views.add_sightings, name='add_sightings'),
    #ex: /SquirrelTracker/sightings/stats/
    path('sightings/stats/', views.stats, name='stats'),
]
