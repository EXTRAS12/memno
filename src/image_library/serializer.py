from rest_framework import serializers

from src.base.services import delete_old_file

from ..user.serializer import AuthorSerializer
from . import models


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class CreateImageSerializer(BaseSerializer):
    class Meta:
        model = models.Image
        fields = ("id", "description", "image", "created_at")

    def update(self, instance, validated_data):
        delete_old_file(instance.image.path)
        return super().update(instance, validated_data)


class CreateFavouriteListSerializer(BaseSerializer):
    class Meta:
        model = models.FavouriteImage
        fields = ("id", "title", "cover", "images")

    def update(self, instance, validated_data):
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class FavouriteListSerializer(CreateFavouriteListSerializer):
    images = CreateImageSerializer(many=True)


class CommentAuthorSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""

    class Meta:
        model = models.Comment
        fields = ("id", "text", "image")


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""

    user = AuthorSerializer()

    class Meta:
        model = models.Comment
        fields = ("id", "text", "user", "image", "created_at")
