from django.core.management.base import BaseCommand
import feedparser
import time
from web_interface.models import Posts, Tags


class Command (BaseCommand):
    help = 'Tags update'

    def handle(self, *args, **options):

        tags = Tags.objects.all()

        posts = Posts.objects.all()

        for post in posts:
            for tag in tags:
                if (tag.tag.lower() in post.title.lower()) or (tag.tag.lower() in post.text.lower()):
                    post.post_tags.add(tag)

