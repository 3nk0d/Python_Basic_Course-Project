from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from web_interface.models import Posts, RSS_links, Tags, Subscribe
from django.contrib.auth.models import User
from web_interface.forms import RSS_links_CreateForm
# Create your views here.

def main_page(request):
    return render(request, 'web_interface/index.html')

class Posts_CreateView(CreateView):
    model = Posts
    fields = ('title', 'text', 'source_link', 'datetime_string', 'rss_link', 'post_tags')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Posts_ListView(ListView):
    model = Posts

    def get_queryset(self):
        if self.request.user.is_staff:
            return super(Posts_ListView, self).get_queryset()
        print(Posts.objects.all())
        return super(Posts_ListView, self).get_queryset().filter(post_tags__in=self.request.user.subscribe.user_tags.all())


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
    form_class = RSS_links_CreateForm
    success_url = reverse_lazy('sources')


class RSS_links_DetailView(DetailView):
    model = RSS_links


class RSS_links_Delete(DeleteView):
    model = RSS_links
    success_url = reverse_lazy('sources')


class Tags_CreateView(CreateView):
    model = Tags
    fields = ('tag',)
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
    fields = ('title', 'text', 'source_link', 'datetime_string', 'rss_link', 'post_tags')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Users_UpdateView(UpdateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('users')
    template_name = 'web_interface/users_form.html'


class AddTag_View(UpdateView):
    model = Subscribe
    fields = ('user_tags',)
    success_url = reverse_lazy('tags')


class RSS_links_UpdateView(UpdateView):
    model = RSS_links
    fields = ('name', 'link', 'approved')
    success_url = reverse_lazy('sources')


class Tags_UpdateView(UpdateView):
    model = Tags
    fields = ('tag',)
    success_url = reverse_lazy('tags')


