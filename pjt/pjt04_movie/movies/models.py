from django.db import models
from accounts.models import User

# Create your models here.
class Movie(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.TextField()
    movie_image = models.ImageField(blank=True)