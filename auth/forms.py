from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        super().save(commit=False)
        self.instance.set_password(self.cleaned_data['password'])
        self.instance.save()
        return self.instance
