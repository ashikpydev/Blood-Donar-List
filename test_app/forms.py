from django import forms

from .models import *


class BloodDonarForm(forms.ModelForm):
    class Meta:
        model = BloodDonar
        fields = ('image',)