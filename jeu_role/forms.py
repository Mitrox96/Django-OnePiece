from dataclasses import field
from django.forms import ModelForm
from .models import role

class formulaire_role(ModelForm):
    class Meta:
        model = role
        fields = '__all__'