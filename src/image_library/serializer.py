from rest_framework import serializers

from src.base.services import delete_old_file

from . import models


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class CreateImageSerializer(BaseSerializer):
    class Meta:
        model = models.Image
        fields = ("id", "description", "image", "created_at")

    def update(self, instance, validated_data):
        delete_old_file(instance.file.path)
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
