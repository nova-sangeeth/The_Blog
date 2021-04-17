from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username
