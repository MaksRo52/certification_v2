from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_password, validate_email

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):

    username = models.CharField(
        max_length=250,
        verbose_name="Логин",
        help_text="Введите ваш логин, например i.ivanov",
        unique=True,
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Номер телефона",
        help_text="Введите номер мобильного телефона",
        **NULLABLE
    )
    password = models.CharField(verbose_name="Пароль", validators=[validate_password])
    email = models.EmailField(unique=True,verbose_name="Электронная почта" ,validators=[validate_email])
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", help_text="Введите вашу дату рождения", **NULLABLE
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата редактирования")


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
