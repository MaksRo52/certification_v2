from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):

    username = models.CharField(
        max_length=250,
        verbose_name="Логин",
        help_text="Введите ваш логин, например i.ivanov",
        unique=True,
    )
    password = models.CharField(
        max_length=128,
        verbose_name="Пароль",
        help_text="Введите ваш пароль",
        **NULLABLE,
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
        help_text="Введите номер мобильного телефона",
        blank=True,
        **NULLABLE
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите вашу дату рождения",
        blank=True,
        null=True,
        **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата редактирования")


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
