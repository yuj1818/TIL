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

1. location이 '독도'인 차고지가 없다면 새 데이터를 생성 후 조회하여 출력
Garage.objects.get_or_create(location='독도', capacity=40, is_parking_available=True, opening_time='07:00', closing_time='22:00')

2. 현재 capacity가 30이하인 차고지를 모두 모아 출력
Garage.objects.filter(capacity__lte=30)

3. 현재 주차 가능 여부가 True인 차고지를 모두 조회하고 조회한 모든 차고지의 location을 각각 출력
for garage in Garage.objects.filter(is_parking_available=True):        
    print(garage.location)
'''