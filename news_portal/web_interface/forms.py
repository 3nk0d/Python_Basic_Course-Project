from django import forms
from web_interface.models import RSS_links

class RSS_links_AdminCreateForm(forms.ModelForm):

    class Meta:
        model = RSS_links
        fields = ('name', 'approved', 'link')


class RSS_links_UserCreateForm(forms.ModelForm):

    class Meta:
        model = RSS_links
        fields = ('name', 'link')
