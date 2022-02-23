from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    # DRAFT = "DRAFT", "Черновик"


class Advertisement(models.Model):
    title = models.TextField(verbose_name='заголовок')
    description = models.TextField(default='', verbose_name='описание')
    status = models.TextField(choices=AdvertisementStatusChoices.choices, default=AdvertisementStatusChoices.OPEN)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='создатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
