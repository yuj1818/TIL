from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.month}/{self.created_at.day}에 생성된 {self.id}번글 - {self.title} : {self.content}'
    
'''
shell_plus 실행 명령어

1. Article(class)로부터 article(instance) 생성
article = Article()
2. 인스턴스 변수(title)에 값을 할당
article.title = 'first'
3. 인스턴스 변수(content)d에 값을 할당
article.content = 'django!'
4. 저장
article.save()
5. 전체 쿼리셋 조회
Article.objects.all()
'''