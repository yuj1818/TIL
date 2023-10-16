from django.db import models
from django.conf import settings

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    address = models.TextField(max_length=100)
    is_franchise = models.TextField(max_length=250)

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    store = models.ForeignKey(Store, models.CASCADE)
    name = models.TextField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    adult = models.IntegerField()