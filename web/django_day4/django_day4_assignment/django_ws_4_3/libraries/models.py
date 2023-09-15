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

1. 첫 번째 데이터 수정
Book.objects.filter(pk=1).update(title='홍길동전', author='허균', pubdate='1994-07-25', price=3000, adult=False)

2. 두 번째 데이터 수정
Book.objects.filter(pk=2).update(title='난중일기', author='이순신', pubdate='2015-01-21', price=0, adult=True)

3. 세 번째 데이터 수정
Book.objects.filter(pk=3).update(title='세종실록', author='이도', pubdate='1397-05-15', price=0, adult=False)

4. 모든 데이터 조회
Book.objects.all().values()

5. 모든 데이터 삭제
Book.objects.all().delete()
'''