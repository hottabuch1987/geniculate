import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.timesince import timesince
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    GENDER_TYPES = (
        ("women", 'женщина'),
        ("men", 'мужчина'),
    )
    bio = models.TextField('Описание', max_length=500, blank=True)
    location = models.CharField('Адрес', max_length=30, blank=True)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    avatar = models.ImageField("Фото", upload_to='avatars', blank=True, null=True)
    gender = models.CharField("Пол", choices=GENDER_TYPES, max_length=10)

    def last_login_formatted(self):
        return timesince(self.last_login)

    def __str__(self):
        return f'{self.username}: {self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email', max_length=50)
    message = models.TextField('Сообщение', max_length=250)

    def __str__(self):
        return f'{self.name}:{self.email}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'





