from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from web_interface.models import Posts, RSS_links, Tags, Subscribe
from django.contrib.auth.models import User
from web_interface.forms import (
    RSS_links_UserCreateForm,
    RSS_links_AdminCreateForm,
    AddTag_View_AdminForm,
    AddTag_View_UserForm,
    Tags_Create_Update_View_Form,
    Posts_Create_Update_View_Form,
)
# Create your views here.
from django.dispatch import receiver
from django.db.models.signals import post_save
from web_interface.tasks import posts_tags_update


def main_page(request):
    return render(request, 'web_interface/index.html')


class Posts_CreateView(CreateView):
    model = Posts
    form_class = Posts_Create_Update_View_Form
    success_url = reverse_lazy('posts')


class Posts_ListView(ListView):
    model = Posts

    def get_queryset(self):
        if self.request.user.is_staff:
            print(self.request)
            return super(Posts_ListView, self).get_queryset()
        return super(Posts_ListView, self).get_queryset().filter(post_tags__in=self.request.user.subscribe.user_tags.all()).distinct()


class Posts_DetailView(DetailView):
    model = Posts


class Posts_Delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('posts')


class Users_CreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('users')
    template_name = 'web_interface/users_form.html'


class Users_ListView(ListView):
    model = User
    template_name = 'web_interface/users_list.html'

class Users_DetailView(DetailView):
    model = User
    template_name = 'web_interface/users_detail.html'

class Users_Delete(DeleteView):
    model = User
    success_url = reverse_lazy('users')
    template_name = 'web_interface/users_confirm_delete.html'

class RSS_links_ListView(ListView):
    model = RSS_links


class RSS_links_CreateView(CreateView):
    model = RSS_links
    success_url = reverse_lazy('sources')

    def get_form_class(self):
        if self.request.user.is_staff:
            return RSS_links_AdminCreateForm
        return RSS_links_UserCreateForm


class RSS_links_DetailView(DetailView):
    model = RSS_links


class RSS_links_Delete(DeleteView):
    model = RSS_links
    success_url = reverse_lazy('sources')


class Tags_CreateView(CreateView):
    model = Tags
    form_class = Tags_Create_Update_View_Form
    success_url = reverse_lazy('tags')


class Tags_ListView(ListView):
    model = Tags

    def get_queryset(self):
        if self.request.user.is_staff:
            return super(Tags_ListView, self).get_queryset()
        return self.request.user.subscribe.user_tags.all()


class Tags_DetailView(DetailView):
    model = Tags


class Tags_Delete(DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')


class Posts_UpdateView(UpdateView):
    model = Posts
    form_class = Posts_Create_Update_View_Form
    success_url = reverse_lazy('posts')


class Users_UpdateView(UpdateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('users')
    template_name = 'web_interface/users_form.html'


class AddTag_View(UpdateView):
    model = Subscribe
    success_url = reverse_lazy('tags')

    def get_form_class(self):
        if self.request.user.is_staff:
            return AddTag_View_AdminForm
        return AddTag_View_UserForm

    def get_queryset(self):
        if self.request.user.is_staff:
            return super(AddTag_View, self).get_queryset()
        return super(AddTag_View, self).get_queryset().filter(id=self.request.user.id)

class RSS_links_UpdateView(UpdateView):
    model = RSS_links
    form_class = RSS_links_AdminCreateForm
    success_url = reverse_lazy('sources')


class Tags_UpdateView(UpdateView):
    model = Tags
    form_class = Tags_Create_Update_View_Form
    success_url = reverse_lazy('tags')


@receiver(post_save, sender=User)
def create_subscribe_for_user_on_save(sender, instance, created, **kwargs):
    if created:
        Subscribe.objects.create(user=instance)
        instance.subscribe.save()


@receiver(post_save, sender=Tags)
def create_subscribe_for_user_on_save(sender, instance, created, **kwargs):
    if created:
        posts_tags_update.delay(instance.tag)
        # posts = Posts.objects.all()
        # for post in posts:
        #     if (instance.tag.lower() in post.title.lower()) or (instance.tag.lower() in post.text.lower()):
        #         post.post_tags.add(instance)
        #         print(post.title)
