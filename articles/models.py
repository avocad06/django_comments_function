from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    # 모델이 변경되는 거라서 기존에 있던 행들의 user필드의 레코드를 어떻게 처리할 것인지
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
class Comment(models.Model):
    content = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)