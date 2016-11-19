from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    feedback = models.TextField(null=True, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.email)


class Topic(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    when = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.id)


class Opinion(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    content = models.CharField(max_length=250)
    when = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
