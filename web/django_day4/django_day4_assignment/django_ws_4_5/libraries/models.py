from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField(default=False)
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        params = {
            'ttbkey': '발급 받은 인증키',
            'QueryType': 'ItemNewAll',
            'MaxResults' : 10,
            'SearchTarget': 'Book',
            'start' : 1,
            'output' : 'js',
            'Version' : '20131101'
        }

        response = requests.get(URL, params=params).json()

        for info in response['item']:
            book = cls(
                    isbn=info['isbn'], 
                    author=info['author'], 
                    title=info['title'], 
                    category_name=info['categoryName'],
                    category_id=info['categoryId'],
                    price=info['priceSales'],
                    fixed_price=info['fixedPrice'],
                    pub_date=info['pubDate']
                )
            book.save()

'''
shell_plus에서 아래 코드 실행
Book.insert_data()
'''