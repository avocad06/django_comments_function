# Generated by Django 3.2.13 on 2022-11-26 13:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(related_name='likes_article', to=settings.AUTH_USER_MODEL),
        ),
    ]