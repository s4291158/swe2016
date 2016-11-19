from django.db import models
from django.contrib.auth.models import User


class StrMixin:
    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.id)


class Interest(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    feedback = models.TextField(null=True, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.email)


class Topic(StrMixin, models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    when = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)


class Side(StrMixin, models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    title = models.CharField(max_length=128)


class Opinion(StrMixin, models.Model):
    side = models.ForeignKey(Side, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    content = models.CharField(max_length=250, unique=True)
    likes = models.IntegerField(default=0)
    when = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
