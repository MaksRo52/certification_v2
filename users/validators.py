from django.core.exceptions import ValidationError


def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Пароль должен содержать не менее 8 символов.")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
    if not any(char.isalpha() for char in value):
        raise ValidationError("Пароль должен содержать хотя бы одну букву.")
    return value


def validate_email(value):
    allowed_domains = {"mail.ru", "yandex.ru"}
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError("Разрешены только адреса mail.ru и yandex.ru")
    return value
