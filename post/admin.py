from django.contrib import admin
from .models import Post, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', 'created_by']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'multi_images']


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
