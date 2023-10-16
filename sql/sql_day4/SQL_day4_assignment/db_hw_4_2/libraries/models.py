from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=200)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    content = models.TextField(max_length=250)