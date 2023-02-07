from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class RSS_links(models.Model):
    name = models.CharField(max_length=40, unique=True)
    link = models.URLField()


class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    source_link = models.URLField()
    rss_link = models.ForeignKey(RSS_links, on_delete=models.PROTECT)


class Tags(models.Model):
    tag = models.CharField(max_length=50, blank=False, unique=True)
    users_tags = models.ManyToManyField(Users)