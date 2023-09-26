
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.
class Memo(models.Model):

    summary = models.CharField(max_length=20)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        blank = True,
        upload_to = 'images',
        processors=[ResizeToFit(200, 200)],
    )
    