from django.contrib import admin
from .models import Place, Image



# @admin.register(Place)
# class PostAdmin(admin.ModelAdmin):
#     raw_id_fields = ('likes',)

admin.site.register(Place)
admin.site.register(Image)