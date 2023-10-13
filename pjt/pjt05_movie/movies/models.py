from django.db import models
from django.conf import settings

class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    content = models.CharField(max_length=200)