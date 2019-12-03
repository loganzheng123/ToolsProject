import csv
  
from django.core.management.base import BaseCommand, CommandError
from SquirrelTracker.models import Squirrel_Census

class Command(BaseCommand):
    help = 'Export squirrel data to csv file'

    def add_arguments(self,parser):
        parser.add_argument('csv_path')

    def handle(self,*args,**options):
        csv_path = options['csv_path']

        fields = ('latitude','longitude','unique_squirrel_id','shift','date','age','primary_fur_color','location',
        'specific_location','running','chasing','climbing','eating','foraging','other_activities','kuks',
        'quaas','moans','tail_flags','tail_twitches','approaches','indifferent','runs_from')

        f = open(csv_path,'w+')
        writer = csv.writer(f)
        writer.writerow(fields)
        for obj in Squirrel_Census.objects.all():
            row = [getattr(obj,field) for field in fields]
            writer.writerow(row)
        f.close()
        print(f'Squirral data has been wrtten to {csv_path}')
