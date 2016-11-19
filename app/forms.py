from .models import Interest
from django import forms


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'
