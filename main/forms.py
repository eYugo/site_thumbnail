from django import forms
from django.db import models
from .models import Thumbnail, Vote, Post


class VoteForm(forms.ModelForm):

    thumbnail = forms.ModelChoiceField(
        label='Escolha uma thumbnail', widget=forms.Select, queryset=Thumbnail.objects.all())

    class Meta:
        model = Vote
        fields = ('thumbnail',)


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
