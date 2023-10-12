from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    red_team = models.TextField(max_length=100)
    blue_team = models.TextField(max_length=100)

class Comment(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    pick = models.BooleanField()
    content = models.TextField(max_length=100)