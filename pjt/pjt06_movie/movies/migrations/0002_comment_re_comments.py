# Generated by Django 4.2.6 on 2023-10-20 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='re_comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_comment', to='movies.comment'),
        ),
    ]
