from django.contrib import admin

from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_display_links = ("user",)
    list_filter = (
        "user",
        "created_at",
    )
    search_fields = ("user",)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "image")
    list_display_links = ("user",)


@admin.register(models.FavouriteImage)
class FavouriteImageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title")
    list_display_links = ("user",)
    search_fields = ("user", "images__title")
