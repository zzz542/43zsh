from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    title = models.CharField(max_length=100, verbose_name="歌曲名字")
    description = models.CharField(max_length=250, verbose_name="歌曲简介")
    image = models.ImageField(upload_to='music/static/', verbose_name="歌曲图片")
    url = models.URLField(blank=True, verbose_name="歌曲链接")
    # Create your models here.


class Meta:
    verbose_name = "音乐"
    verbose_name_plural = "音乐"


def _str_(self):
    return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()


def __str__(self):
    return self.text
