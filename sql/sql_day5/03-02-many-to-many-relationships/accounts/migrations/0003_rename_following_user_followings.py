# Generated by Django 4.2.5 on 2023-10-17 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='followings',
        ),
    ]