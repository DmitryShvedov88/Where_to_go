from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'get_preview', 'number_image']
    readonly_fields = ["get_preview"]
    def get_preview(self, obj):
        return format_html('<img src="{url}" width="auto" height="300px"/>'.format(url = obj.image.url))


@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['get_preview']
    readonly_fields = ["get_preview"]
    def get_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="300px" />'.format(obj.image.url))
