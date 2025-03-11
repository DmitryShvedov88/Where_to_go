from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Место", blank=True, null=True)
    short_description = models.CharField(max_length=250, verbose_name='Короткое описание', blank=True, null=True)
    long_description = HTMLField(verbose_name='Длинное описание', blank=True, null=True)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name="Картинка места", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name="КАРТИНКА", db_index=True, upload_to="images/")
    number = models.IntegerField(verbose_name="ПОЗИЦИЯ", db_index=True, default=0)

    def __str__(self):
        return f"{self.number}. {self.place.title}"

    class Meta:
        ordering = ['number']
