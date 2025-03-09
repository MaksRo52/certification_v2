from datetime import date

from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = {"ерунда", "глупость", "чепуха"}


def validate_age(value):
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )
    if age < 18:
        raise ValidationError("Вам должно быть не меньше 18 лет для публикации постов")
    return value


def validate_title(value):
    if not value:
        raise ValidationError("Укажите заголовок поста")
    if any(word in value.lower() for word in FORBIDDEN_WORDS):
        raise ValidationError("Нельзя использовать запрещенные слова в заголовке поста")
    return value
