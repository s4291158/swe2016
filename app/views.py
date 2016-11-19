from django.shortcuts import render
from django.views import View
from .forms import InterestForm
from django.http import JsonResponse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class LandingView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': InterestForm()
        }
        return render(request, 'landing.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['errors'] = form.errors
        return JsonResponse(context)
