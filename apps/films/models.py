from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assisted_in = models.DateField(blank=True, null=True)
    would_like = models.BooleanField()