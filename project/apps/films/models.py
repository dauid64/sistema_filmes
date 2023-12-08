from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    assisted_in = models.DateField(blank=True, null=True)
    would_like = models.BooleanField()


class FilmExportRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.FileField(upload_to='films/exports/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(null=True, blank=True)


class FilmImportRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.FileField(upload_to='films/imports/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(null=True, blank=True)