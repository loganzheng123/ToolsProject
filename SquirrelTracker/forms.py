from django.forms import ModelForm

from .models import Squirrel_Census

class SightingForm(ModelForm):
    class Meta:
        model = Squirrel_Census
        fields='__all__'
