from colorfield.fields import ColorField
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    color = ColorField(verbose_name='Цвет')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    short_desc = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание')
    type = models.ForeignKey(
        to=Type, on_delete=models.CASCADE, db_index=True,
        related_name='news', verbose_name='Тип'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name
