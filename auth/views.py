from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views import View

from .forms import RegisterForm


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['errors'] = form.errors
        return JsonResponse(context)


class LoginView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            context['success'] = True
        else:
            context['errors'] = form.errors
        return JsonResponse(context)
