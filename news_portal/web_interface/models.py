from django.db import models

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.tag

class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_tags = models.ManyToManyField(Tags)


class RSS_links(models.Model):
    name = models.CharField(max_length=40, unique=True)
    approved = models.BooleanField()
    link = models.URLField()

    def __str__(self):
        return self.name

class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    source_link = models.URLField()
    datetime_string = models.CharField(max_length=100)
    rss_link = models.ForeignKey(RSS_links, on_delete=models.PROTECT)
    post_tags = models.ManyToManyField(Tags)
