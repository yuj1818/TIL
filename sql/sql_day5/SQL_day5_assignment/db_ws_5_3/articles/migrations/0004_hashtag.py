# Generated by Django 3.2.7 on 2023-10-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, unique=True)),
                ('hashtags', models.ManyToManyField(blank=True, to='articles.Article')),
            ],
        ),
    ]
