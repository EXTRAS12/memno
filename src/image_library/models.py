from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import (
    get_path_upload_cover_favourite_image,
    get_path_upload_image,
    validate_size_image,
)
from src.user.models import AuthUser


class Image(models.Model):
    """Модель для загрузки мема"""

    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name="images"
    )
    description = models.TextField(max_length=1500, verbose_name="Описание")
    image = models.ImageField(
        upload_to=get_path_upload_image,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"]),
            validate_size_image,
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    user_of_likes = models.ManyToManyField(
        AuthUser, related_name="likes_of_image"
    )

    def __str__(self):
        return f"{self.user}"


class Comment(models.Model):
    """Модель комментариев к мему"""

    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name="comments"
    )
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name="image_comments"
    )
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class FavouriteImage(models.Model):
    """Модель избранного для пользователя"""

    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name="favourites_lists"
    )
    title = models.CharField(max_length=100)
    images = models.ManyToManyField(
        Image, related_name="image_favourites_lists"
    )
    cover = models.ImageField(
        upload_to=get_path_upload_cover_favourite_image,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"]),
            validate_size_image,
        ],
    )
