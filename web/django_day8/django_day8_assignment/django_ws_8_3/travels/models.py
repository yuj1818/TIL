from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit

class Travel(models.Model):
    location = models.CharField(max_length=10)
    plan = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = ProcessedImageField(
        blank = True,
        processors = [ResizeToFit(200, 200)]
    )
    thumbnail = ImageSpecField(
        source = 'image',
        processors = [ResizeToFit(100, 100)],
        options = {'quality': 90}
    )
