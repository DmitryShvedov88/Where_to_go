from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Место", blank=True, null=True)
    short_description =  models.CharField(max_length=250, verbose_name='Короткое описание', blank=True, null=True)
    long_descriptio = models.TextField(verbose_name='Длинное описание', blank=True, null=True)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    def __str__(self):
        return self.title
