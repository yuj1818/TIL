from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id}번째 영화 - {self.title}( {self.genre} )'
    
    '''
    shell_plus 명령어
    1. 데이터 객체 생성
    Movie.objects.create(title='Venom: Let There Be Carnage', genre='action')
    Movie.objects.create(title='Ron’s Gone Wrong', genre='animation')
    Movie.objects.create(title='007 No Time To Die', genre='action')
    Movie.objects.create(title='Dune', genre='adventure')
    2. model의 전체 쿼리셋을 id에 대해 내림차순으로 조회
    Movie.objects.all().order_by('-id')
    3. model의 전체 쿼리셋 중 genre가 action인 것만 조회
    Movie.objects.filter(genre="action") 
    4. model의 전체 쿼리셋 중 title이 e로 끝나는 것만 조회
    Movie.objects.filter(title__endswith="e")
    '''