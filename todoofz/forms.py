from django import forms
# from django.contrib.auth.models import Group
# from django.forms import ModelForm
from todoofz.models import Category, Task

class SearchForm(forms.Form):
    """Search."""

    q = forms.CharField(widget=forms.widgets.TextInput(attrs={"size": 35}))
