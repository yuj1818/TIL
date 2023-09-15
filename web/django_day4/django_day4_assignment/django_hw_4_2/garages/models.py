from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

'''
shell_plus 명령어

Garage에 2개의 데이터 생성
Garage.objects.create(location='서울', capacity=30, is_parking_available=False, opening_time='08:00', closing_time='22:00')
Garage.objects.create(location='부산', capacity=20, is_parking_available=True, opening_time='07:00', closing_time='23:00')
'''