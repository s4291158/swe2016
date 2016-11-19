from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    feedback = models.TextField(null=True, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.email)
