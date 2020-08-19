from django import forms
from django.db import models
from .models import Thumbnail, Vote, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'descricao')


class ThumbnailCreateForm(forms.ModelForm):

    class Meta:
        model = Thumbnail
        fields = ('titulo', 'imagem',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'descricao')


class ThumbnailUpdateForm(forms.ModelForm):
    class Meta:
        model = Thumbnail
        fields = ('titulo', 'imagem',)
