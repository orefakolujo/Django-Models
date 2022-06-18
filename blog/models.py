from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "post"
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = get_user_model()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

