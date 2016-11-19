from django.contrib.auth import login, authenticate, logout
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
            user = authenticate(**form.cleaned_data)
            login(request, user)
            context['success'] = True
            context['user_id'] = user.id
        else:
            context['errors'] = form.errors
        return JsonResponse(context)


class LoginView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            context['success'] = True
            context['user_id'] = user.id
        else:
            context['errors'] = form.errors
        return JsonResponse(context)


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        context = {'success': True}
        return JsonResponse(context)
