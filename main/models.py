from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def restrict_amount(value):
    if Thumbnail.objects.filter(post_id=value).count() >= 6:
        raise ValidationError(
            'Post already has maximal amount of thumbnails (6)')


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo


class Thumbnail(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='thumbnail_imgs')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    num_votos = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Vote(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Thumbnail = models.ForeignKey(Thumbnail, on_delete=models.CASCADE)
