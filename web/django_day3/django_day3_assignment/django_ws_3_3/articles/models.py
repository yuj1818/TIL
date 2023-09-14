from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'
    
    '''
    shell_plus 명령어

    1. 데이터 객체 생성
    Article.objects.create(title='first', content='WE')
    Article.objects.create(title='second', content='ARE')
    Article.objects.create(title='third', content='GGANBU')
    '''