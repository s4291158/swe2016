from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views import View

from auth.forms import RegisterForm
from .forms import InterestForm, OpinionForm
from .models import Topic, Opinion


def include_auth(context):
    context.update({
        'login_form': AuthenticationForm(),
        'register_form': RegisterForm()
    })
    return context


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class LandingView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': InterestForm()
        }
        context = include_auth(context)
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
        context = {
            'form': OpinionForm()
        }
        topic_id = kwargs['topic_id']
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            return Http404()
        context['topic'] = topic.__dict__
        side_set = []
        for side in topic.side_set.all():
            side_data = {
                'id': side.id,
                'title': side.title,
                'opinion_set': side.opinion_set.order_by('-likes')[0:40]
            }
            side_data['showing'] = '{}/{}'.format(
                len(side_data['opinion_set']), side.opinion_set.count()
            )
            side_set.append(side_data)
        context['topic']['side_set'] = side_set
        context = include_auth(context)
        return render(request, 'topic.html', context)


class OpinionView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['errors'] = form.errors
        return JsonResponse(context)


class LikeView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        if 'liked_opinions' in request.session:
            id_set = request.session['liked_opinions']
        else:
            id_set = []
        try:
            opinion_id = int(request.POST['opinion_id'])
        except ValueError:
            pass
        else:
            try:
                opinion = Opinion.objects.get(id=opinion_id)
            except Opinion.DoesNotExist:
                pass
            else:
                if opinion_id not in id_set:
                    opinion.likes += 1
                    opinion.save()
                    id_set.append(opinion.id)
                    context['liked'] = True
                else:
                    opinion.likes -= 1
                    opinion.save()
                    id_set.remove(opinion_id)
                    context['liked'] = False
                request.session['liked_opinions'] = id_set
                context['success'] = True
                context['likes'] = opinion.likes
                return JsonResponse(context)

        context['success'] = False
        return JsonResponse(context)
