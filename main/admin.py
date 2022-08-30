from django.contrib import admin
from .models import Blog, BlogImages


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogImages)
