from django.core.management.base import BaseCommand
from web_interface.models import Posts, Users, RSS_links, Tags


class Command (BaseCommand):
    help = 'Fill DB'

    def handle(self, *args, **options):
        #Tags.objects.all().delete()
        #RSS_links.objects.all().delete()
        #Users.objects.all().delete()
        #Posts.objects.all().delete()

        tag1 = Tags.objects.create(tag='найден')
        tag2 = Tags.objects.create(tag='взломан')
        tag3 = Tags.objects.create(tag='авария')
        tag4 = Tags.objects.create(tag='яндекс')


        user1 = Users.objects.create(username='Vovan3', name='Vova', email='Vova@email.com')
        user2 = Users.objects.create(username='Ivan12', name='Ivan', email='Ivan@email.com')
        user3 = Users.objects.create(username='Ann4', name='Anna', email='Anna@email.com')

        user1.user_tags.add(tag1, tag4)
        user2.user_tags.add(tag2)
        user3.user_tags.add(tag2, tag3, tag4)

        first_url = RSS_links.objects.create(name='first', approved=False, link='http://www.google.com')
        second_url = RSS_links.objects.create(name='second', approved=False, link='http://www.yandex.com')
        third_url = RSS_links.objects.create(name='swyx.io', approved=True, link='https://swyx.io/rss.xml')

        post1 = Posts.objects.create(title='Cool title 1', text='The best text 1', source_link='some url 1', rss_link=first_url)
        # post1.rss_link.add(first_url)
        # post1.save()
        # rss_link1 = post1.rss_link.all()
        # for item in rss_link1:
        #     print(rss_link1.name)
        post2 = Posts.objects.create(title='Cool title 2', text='The best text 2', source_link='some url 2', rss_link=first_url)
        #post2.rss_link.add(first_url)
        post3 = Posts.objects.create(title='Cool title 3', text='The best text 3', source_link='some url 3', rss_link=second_url)
        #post3.rss_link.add(second_url)
        post4 = Posts.objects.create(title='Cool title 4', text='The best text 4', source_link='some url 4', rss_link=second_url)
        #post4.rss_link.add(second_url)

        post1.post_tags.add(tag1)
        post2.post_tags.add(tag2, tag3)
        post3.post_tags.add(tag4)
        post4.post_tags.add(tag1, tag3)
