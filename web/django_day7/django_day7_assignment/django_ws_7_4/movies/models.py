from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    synopsis = models.TextField()
    image = ProcessedImageField(
        blank = True,
        upload_to='images',
        processors=[ResizeToFit(width=200, upscale=False)],
        )
    thumbnail = ImageSpecField(
        source = 'image',
        processors = [ResizeToFit(100, 100)],
        options = {'quality': 90}
        )
    