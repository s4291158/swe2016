from django.shortcuts import render
from django.views import View
from .forms import InterestForm
from django.http import JsonResponse, Http404
from .models import Topic


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


class TopicView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        topic_id = kwargs['topic_id']
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return Http404()
        context['topic'] = topic
        return render(request, 'topic.html', context)
