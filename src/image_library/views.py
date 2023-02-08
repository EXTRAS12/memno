import os

from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, parsers, views, viewsets

from ..base.classes import MixedSerializer, Pagination
from ..base.permissions import IsAuthor
from ..base.services import delete_old_file
from . import models, serializer


class ImageView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD картинок"""

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = serializer.CreateImageSerializer
    serializer_classes_by_action = {"list": serializer.CreateImageSerializer}

    def get_queryset(self):
        return models.Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.image.path)
        instance.delete()


class FavouriteImageListView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD для избранных картинок"""

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = serializer.CreateFavouriteListSerializer
    serializer_classes_by_action = {"list": serializer.FavouriteListSerializer}

    def get_queryset(self):
        return models.FavouriteImage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class ImageListView(generics.ListAPIView):
    """Список всех картинок"""

    queryset = models.Image.objects.all()
    serializer_class = serializer.CreateImageSerializer
    pagination_class = Pagination


class AuthorImageListView(generics.ListAPIView):
    """Список всех картинок автора"""

    serializer_class = serializer.CreateImageSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return models.Image.objects.filter(user__id=self.kwargs.get("pk"))


class CommentAuthorView(viewsets.ModelViewSet):
    """CRUD комментариев автора"""

    serializer_class = serializer.CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return models.Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    """Комментарии к картинке"""

    serializer_class = serializer.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(image_id=self.kwargs.get("pk"))


class StreamImageView(views.APIView):
    """Просмотр картинки"""

    def get(self, request, pk):
        self.image = get_object_or_404(models.Image, id=pk)
        if os.path.exists(self.image.image.path):
            return FileResponse(
                open(self.image.image.path, "rb"),
                filename=self.image.image.name,
            )
        else:
            return Http404


class DownloadImageView(views.APIView):
    """Скачивание картинки"""

    def get(self, request, pk):
        self.image = get_object_or_404(models.Image, id=pk)
        if os.path.exists(self.image.image.path):
            return FileResponse(
                open(self.image.image.path, "rb"),
                filename=self.image.image.name,
                as_attachment=True,
            )
        else:
            return Http404
