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
    AddTag_View,
)
from users.views import (
    Registration_View,
    Login_View,
    Logout_View,
    Account,
    Account_Update,
    Account_Password_Update,
)


urlpatterns = [
    path('', main_page, name='main'),
    path('posts/', Posts_ListView.as_view(), name='posts'),
    path('posts/<int:pk>/', Posts_DetailView.as_view(), name='post'),
    path('posts/create/', Posts_CreateView.as_view(), name='post_create'),
    path('posts/change/<int:pk>/', Posts_UpdateView.as_view(), name='post_change'),
    path('posts/delete/<int:pk>/', Posts_Delete.as_view(), name='post_delete'),
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
    path('subscribe/change/<int:pk>/', AddTag_View.as_view(),name='subcribe_change'),
    #USERS
    path('users/registration/', Registration_View.as_view(), name='registration'),
    path('users/login/', Login_View.as_view(), name='authentication'),
    path('users/logout/', Logout_View.as_view(), name='log_out'),
    path('users/account/<int:pk>/', Account.as_view(), name='account'),
    path('user/update/<int:pk>/', Account_Update.as_view(), name='account_update'),
    path('user/pass_update/<int:pk>/', Account_Password_Update.as_view(), name='account_pass_update'),
    path('admin/', admin.site.urls),
]
