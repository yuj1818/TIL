from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    memo = models.TextField(default="")

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content} / {self.memo}'
    
    '''
    shell_plus 명령어

    1. 데이터 객체 생성
    Article.objects.create(title='first', content='WE')
    Article.objects.create(title='second', content='ARE')
    Article.objects.create(title='third', content='GGANBU')
    2. 첫 번째, 두 번째 레코드의 title을 각각 'finally', 'last'로 update
    article = Article.objects.get(pk=1)
    article.title = 'finally'
    article.save()
    article = Article.objects.get(pk=2)
    article.title = 'last'
    article.save()
    3. 새로운 레코드 추가
    Article.objects.create(title='homework', content='finished', memo='tired')
    4. 첫 번재 레코드 삭제
    article = Article.objects.get(pk=1)
    article.delete()
    5. Article 모델의 전체 쿼리셋 조회
    Article.objects.all()
    '''