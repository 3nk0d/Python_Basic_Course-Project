from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from web_interface.models import Posts, Users, RSS_links, Tags

# Create your views here.

def main_page(request):
    return render(request, 'web_interface/index.html')

class Posts_CreateView(CreateView):
    model = Posts
    fields = ('title', 'text', 'source_link', 'rss_link')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Posts_ListView(ListView):
    model = Posts


class Posts_DetailView(DetailView):
    model = Posts


class Posts_Delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('posts')


class Users_CreateView(CreateView):
    model = Users
    fields = ('username', 'password', 'second_name', 'name', 'email')
    success_url = reverse_lazy('users')


class Users_ListView(ListView):
    model = Users


class Users_DetailView(DetailView):
    model = Users


class Users_Delete(DeleteView):
    model = Users
    success_url = reverse_lazy('users')


class RSS_links_ListView(ListView):
    model = RSS_links


class RSS_links_CreateView(CreateView):
    model = RSS_links
    fields = ('name', 'link')
    success_url = reverse_lazy('sources')


class RSS_links_DetailView(DetailView):
    model = RSS_links


class RSS_links_Delete(DeleteView):
    model = RSS_links
    success_url = reverse_lazy('sources')


class Tags_CreateView(CreateView):
    model = Tags
    fields = ('tag', 'users_tags')
    success_url = reverse_lazy('tags')


class Tags_ListView(ListView):
    model = Tags


class Tags_DetailView(DetailView):
    model = Tags


class Tags_Delete(DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')


class Posts_UpdateView(UpdateView):
    model = Posts
    fields = ('title', 'text', 'source_link', 'rss_link')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Users_UpdateView(UpdateView):
    model = Users
    fields = ('username', 'password', 'second_name', 'name', 'email')
    success_url = reverse_lazy('users')

class RSS_links_UpdateView(UpdateView):
    model = RSS_links
    fields = ('name', 'link')
    success_url = reverse_lazy('sources')

class Tags_UpdateView(UpdateView):
    model = Tags
    fields = ('tag', 'users_tags')
    success_url = reverse_lazy('tags')