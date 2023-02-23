from celery import shared_task
import feedparser
from web_interface.models import Posts, RSS_links, Tags



@shared_task()
def rss_parsing():
    print('start')
    rss_links = RSS_links.objects.filter(approved=True)

    tags = Tags.objects.all()

    for rss_link in rss_links:
        print(rss_link.link)
        response = feedparser.parse(rss_link.link)
        #print(response)
        if not response['entries']:
            continue
        print(response['entries'].len())
        for post in response['entries']:
            try:
                title = post['title']
                summary = post['summary']
                source_link = post['link']
                publish_date_str = post['published']
                publish_date_time_struct = post['published_parsed']
            except Exception:
                continue
            if Posts.objects.filter(title=title):
                continue
            Post = Posts.objects.create(title=title, text=summary, source_link=source_link, datetime_string=publish_date_str, rss_link=rss_link)

            for tag in tags:
                if (tag.tag in title) or (tag.tag in summary):
                    Post.post_tags.add(tag)

    print('end')

@shared_task()
def posts_tags_update(name):
    posts = Posts.objects.all()
    tag = Tags.objects.get(tag=name)
    print(tag)
    name = name.lower()
    for post in posts:
        if (name in post.title.lower()) or (name in post.text.lower()):
            post.post_tags.add(tag)
            print(post.title)
