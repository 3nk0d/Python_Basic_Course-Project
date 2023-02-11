"""news_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_interface.views import (
    main_page,
    Posts_ListView,
    Users_ListView,
    RSS_links_ListView,
    Tags_ListView,
    Posts_DetailView,
    Users_DetailView,
    RSS_links_DetailView,
    Tags_DetailView,
    Posts_Delete,
    Users_Delete,
    RSS_links_Delete,
    Tags_Delete,
    Posts_CreateView,
    Users_CreateView,
    RSS_links_CreateView,
    Tags_CreateView,
    Posts_UpdateView,
    Users_UpdateView,
    RSS_links_UpdateView,
    Tags_UpdateView,
    Posts_User_View,
)
from users.views import (
    Registration_View,
    Authentication_View,
    LogOut_View,
)


urlpatterns = [
    path('', main_page, name='main'),
    path('posts/', Posts_User_View.as_view(), name='posts'),
    path('posts_control/', Posts_ListView.as_view(), name='posts_control'),
    path('posts_control/<int:pk>/', Posts_DetailView.as_view(), name='post'),
    path('posts_control/create/', Posts_CreateView.as_view(), name='post_create'),
    path('posts_control/change/<int:pk>/', Posts_UpdateView.as_view(), name='post_change'),
    path('posts_control/delete/<int:pk>/', Posts_Delete.as_view(), name='post_delete'),
    path('users/', Users_ListView.as_view(), name='users'),
    path('users/<int:pk>/', Users_DetailView.as_view(), name='user'),
    path('users/create/', Users_CreateView.as_view(), name='user_create'),
    path('users/change/<int:pk>/', Users_UpdateView.as_view(), name='user_change'),
    path('users/delete/<int:pk>/', Users_Delete.as_view(), name='user_delete'),
    path('rss_links/', RSS_links_ListView.as_view(), name='sources'),
    path('rss_links/<int:pk>/', RSS_links_DetailView.as_view(), name='source'),
    path('rss_links/create/', RSS_links_CreateView.as_view(), name='source_create'),
    path('rss_links/change/<int:pk>/', RSS_links_UpdateView.as_view(), name='source_change'),
    path('rss_links/delete/<int:pk>/', RSS_links_Delete.as_view(), name='source_delete'),
    path('tags/', Tags_ListView.as_view(), name='tags'),
    path('tags/<int:pk>/', Tags_DetailView.as_view(), name='tag'),
    path('tags/create/', Tags_CreateView.as_view(), name='tag_create'),
    path('tags/change/<int:pk>/', Tags_UpdateView.as_view(), name='tag_change'),
    path('tags/delete/<int:pk>/', Tags_Delete.as_view(), name='tag_delete'),
    #USERS
    path('users/registration/', Registration_View.as_view(), name='registration'),
    path('users/login/', Authentication_View.as_view(), name='authentication'),
    path('users/logout/', LogOut_View.as_view(), name='log_out'),
    path('admin/', admin.site.urls),
]
