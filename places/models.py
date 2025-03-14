from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Место"
        )
    short_description = models.CharField(
        max_length=250,
        verbose_name='Короткое описание',
        blank=True,
        default="Нет описания"
        )
    long_description = HTMLField(
        verbose_name='Длинное описание',
        blank=True,
        default="Нет описания"
        )
    latitude = models.FloatField(
        verbose_name="Широта"
        )
    longitude = models.FloatField(
        verbose_name="Долгота"
        )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name="Картинка места",
        on_delete=models.CASCADE,
        related_name="images"
        )
    image = models.ImageField(
        verbose_name="Картинка",
        db_index=True,
        upload_to="images/"
        )
    number = models.IntegerField(
        verbose_name="Позиция",
        db_index=True,
        default=0
        )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.number}. {self.place.title}"
