import csv

from django.core.management.base import BaseCommand, CommandError
from SquirrelTracker.models import Squirrel_Census

class Command(BaseCommand):
    help = 'Import squirrel data from given csv file'

    def add_arguments(self,parser):
        parser.add_argument('csv_path')
    
    def handle(self,*args,**options):
        csv_path = options['csv_path']
        
        model_fields = [f.name for f in Squirrel_Census._meta.fields]
        fields_name = []
        with open(csv_path,'rt',encoding='latin') as csv_file:
            reader = csv.reader(csv_file,delimiter=',',quotechar='"')
            fields_name = next(reader)
            for i,_ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower()
                if fields_name[i][-1].strip()=='y':
                    fields_name[i]='latitude'
                elif fields_name[i][-1].strip()=='x':
                    fields_name[i]='longitude'
                else:
                    pass
                fields_name[i] = fields_name[i].replace(' ','_')

                    
            for row in reader:
                try:
                    obj = Squirrel_Census()
                    for i,field in enumerate(row):
                        if fields_name[i] in model_fields:
                            if fields_name[i] == 'date':
                                value = str(field)[4:]+'-'+str(field)[:2]+'-'+str(field)[2:4]
                                setattr(obj, fields_name[i],value)
                            else:
                                if str(field).lower()=='true':
                                    value = True
                                    setattr(obj, fields_name[i],value)
                                elif str(field).lower()=='false':
                                    value = False
                                    setattr(obj, fields_name[i],value)
                                else:
                                    setattr(obj, fields_name[i],field)
                        else:
                            pass
                    obj.save()
                except Exception as e:
                    raise CommandError(e)
