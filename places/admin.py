from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['image', 'preview', 'number']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width:250px; max-height:250px"/>',
            obj.image.url
            )


@admin.register(Place)
class PostAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    autocomplete_fields = ['place']
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width:250px; max-height:250px"/>',
            obj.image.url
            )
