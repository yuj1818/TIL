from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

'''
shell_plus 명령어

1. 최소 3개 이상의 데이터 생성
import datetime
today = datetime.datetime.today()
Book.objects.create(title='첫번째 책', author='첫번째 저자', pubdate=today, price=1000, adult=True)
Book.objects.create(title='두번째 책', author='두번째 저자', pubdate=today, price=2000, adult=False)
Book.objects.create(title='세번째 책', author='세번째 저자', pubdate=today, price=2000, adult=False)

2. 생성한 데이터 모두 조회 및 순회하여 각각의 title만 출력
for data in Book.objects.all():
    print(data.title)
'''