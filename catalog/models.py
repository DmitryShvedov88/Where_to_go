from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Место", blank=True, null=True)
    short_description = models.CharField(max_length=250, verbose_name='Короткое описание', blank=True, null=True)
    long_descriptio = models.TextField(verbose_name='Длинное описание', blank=True, null=True)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/")
    number_image = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.number_image}. {self.place.title}"
