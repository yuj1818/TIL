from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

'''
admin 등록
python manage.py createsuperuser
'''