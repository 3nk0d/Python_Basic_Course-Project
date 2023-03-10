from django.core.management.base import BaseCommand
import feedparser
import time
from web_interface.models import Posts, RSS_links, Tags


class Command (BaseCommand):
    help = 'RSS parsing'

    def handle(self, *args, **options):

        rss_links = RSS_links.objects.filter(approved=True)

        tags = Tags.objects.all()

        for rss_link in rss_links:
            print(rss_link.link)
            response = feedparser.parse(rss_link.link)
            if not response['entries']:
                continue
            print(len(response['entries']))
            for post in response['entries']:

                try:
                    title = post['title']
                    summary = post['summary']
                    source_link = post['link']
                    publish_date_str = post['published']
                    publish_date_time_struct = post['published_parsed']
                except Exception as e:
                    print("Post have an empty field:")
                    print(e)
                    print('Post:')
                    print(post)
                    continue

                if Posts.objects.filter(title=title):
                    continue
                try:
                    Post = Posts.objects.create(title=title, text=summary, source_link=source_link, datetime_string=publish_date_str, rss_link=rss_link)
                except Exception as e:
                    print("Post wasn't parsed. Error while write it to DB:")
                    print(e)
                    print('Post:')
                    print(post)

                for tag in tags:
                    if (tag.tag in title) or (tag.tag in summary):
                        Post.post_tags.add(tag)

