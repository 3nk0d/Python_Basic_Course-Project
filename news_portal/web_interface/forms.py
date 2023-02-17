from django import forms
from django.forms import widgets
from web_interface.models import RSS_links, Subscribe

class RSS_links_AdminCreateForm(forms.ModelForm):

    class Meta:
        model = RSS_links
        fields = ('name', 'approved', 'link')


class RSS_links_UserCreateForm(forms.ModelForm):

    class Meta:
        model = RSS_links
        fields = ('name', 'link')


class AddTag_View_AdminForm(forms.ModelForm):

    # user_tags = forms.ModelMultipleChoiceField(queryset=Subscribe.objects.all(),
    #                                            widget=widgets.SelectMultiple(attrs={'size': 20}))

    class Meta:
        model = Subscribe
        fields = ('user', 'user_tags')


class AddTag_View_UserForm(forms.ModelForm):

    #user_tags = forms.ModelMultipleChoiceField(queryset=Subscribe.objects.all(),
    #                                          widget=widgets.SelectMultiple(attrs={'size': 20}))

    class Meta:
        model = Subscribe
        fields = ('user_tags',)
