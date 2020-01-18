from django.contrib import admin
from .models import Post, Category 


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', 'created_by']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
