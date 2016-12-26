from django import forms
from django.contrib.auth.models import User
from main.models import Work, Version
from tinymce.widgets import TinyMCE


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['public', 'title', 'description']

class VersionForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    # text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Version
        fields = ['text']
