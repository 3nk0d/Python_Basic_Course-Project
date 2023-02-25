from django import forms
from django.forms import widgets
from web_interface.models import RSS_links, Subscribe, Tags, Posts
from django.contrib.auth.models import User


class RSS_links_AdminCreateForm(forms.ModelForm):

    name = forms.CharField(label='Название')
    approved = forms.BooleanField(label='Одобрен')
    link = forms.URLField(label='Ссылка')

    class Meta:
        model = RSS_links
        fields = ('name', 'approved', 'link')


class RSS_links_UserCreateForm(forms.ModelForm):

    name = forms.CharField(label='Название')
    link = forms.URLField(label='Ссылка')

    class Meta:
        model = RSS_links
        fields = ('name', 'link')


class AddTag_View_AdminForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Пользователь')
    user_tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='Тэги',
                                               widget=widgets.SelectMultiple(attrs={'size': 18}))

    class Meta:
        model = Subscribe
        fields = ('user', 'user_tags')


class AddTag_View_UserForm(forms.ModelForm):

    user_tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='Тэги',
                                               widget=widgets.SelectMultiple(attrs={'size': 18}))

    class Meta:
        model = Subscribe
        fields = ('user_tags',)


class Tags_Create_Update_View_Form(forms.ModelForm):

    tag = forms.CharField(label='Тэг')

    class Meta:
        model = Tags
        fields = ('tag',)


class Posts_Create_Update_View_Form(forms.ModelForm):

    title = forms.CharField(label='Название')
    text = forms.Field(label='Текст', widget=forms.Textarea)
    source_link = forms.URLField(label='Ссылка на источник')
    datetime_string = forms.CharField(label='Дата и время создания')
    rss_link = forms.ModelChoiceField(queryset=RSS_links.objects, label='Наименование источника')
    #post_tags = forms.MultipleChoiceField(choices=tags, label='Тэги', widget=forms.CheckboxSelectMultiple())
    post_tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='Тэги')

    class Meta:
        model = Posts
        fields = ('title', 'text', 'source_link', 'datetime_string', 'rss_link', 'post_tags')
