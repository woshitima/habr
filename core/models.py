from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    author = models.ForeignKey(
        to = "Author",
        on_delete = models.SET_NULL,
        null = True, blank = True,
        related_name = "article",
        verbose_name = "Автор"
    )

    readers = models.ManyToManyField(
        to = User,
        related_name = "read_articles",
        blank = True,
    )

    views = models.IntegerField(
        default = 0,
        verbose_name = "Просмотры"
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
        null = True,
    )

    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(
        to = User,
        related_name = "author",
        verbose_name = "Пользователь",
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )

    nickname = models.CharField(max_length = 55)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return self.nickname