from django.db import models
from django.conf import settings

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)
    movie = models.CharField(max_length=30)