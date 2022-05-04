from django import forms
from .models import  albums




class albumsForm(forms.ModelForm):
    class Meta:
        model = albums
        field = [
            'title',
            'artist',
            'created_at',
        ]