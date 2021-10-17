from django.db import models
from django.db.models import fields
from django.forms import ModelForm

from .models import Offspring

class OffspringForm(ModelForm):
    class Meta:
        model = Offspring
        fields = ['naam', 'image']