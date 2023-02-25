from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Tags(models.Model):
    tag = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.tag


class Subscribe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_tags = models.ManyToManyField(Tags)


class RSS_links(models.Model):
    name = models.CharField(max_length=40, unique=True)
    approved = models.BooleanField(default=False)
    link = models.URLField()

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    source_link = models.URLField()
    datetime_string = models.CharField(max_length=100)
    rss_link = models.ForeignKey(RSS_links, on_delete=models.PROTECT)
    post_tags = models.ManyToManyField(Tags)
