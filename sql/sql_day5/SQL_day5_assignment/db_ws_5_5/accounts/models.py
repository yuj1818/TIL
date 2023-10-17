from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image_file = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options = {'quality':90}
    )