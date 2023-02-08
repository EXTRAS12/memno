from rest_framework import serializers

from . import models


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ("avatar", "country", "city", "bio", "nickname")


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialLink
        fields = (
            "id",
            "link",
        )


class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = (
            "id",
            "avatar",
            "country",
            "city",
            "bio",
            "nickname",
            "social_links",
        )
