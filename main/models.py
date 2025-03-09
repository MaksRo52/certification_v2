from django.db import models

from main.validators import validate_title, validate_age
from users.models import User

NULLABLE = {"null": True, "blank": True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", validators=[validate_title])
    content = models.TextField(verbose_name="Текст")
    picture = models.ImageField(verbose_name="Изображение", **NULLABLE)
    owner = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.SET_NULL, **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def clean(self):
        if self.owner and self.owner.date_of_birth:
            validate_age(self.owner.date_of_birth)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.owner})"


class Commentary(models.Model):
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.SET_NULL, **NULLABLE
    )
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.content[:100]}... ({self.owner})"
