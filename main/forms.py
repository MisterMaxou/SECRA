from django import forms
from django.contrib.auth.models import User
from main.models import Work, Version
from tinymce.widgets import TinyMCE


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['public', 'title', 'description']

class VersionForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 20, 'id':'version_form', 'placeholder':'Entrez ici la nouvelle version du texte auquel vous voulez contribuer.'}))

    class Meta:
        model = Version
        fields = ['text']
