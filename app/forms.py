from .models import Interest, Opinion
from django import forms


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        exclude = ('likes',)
