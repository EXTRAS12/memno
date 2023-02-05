import os

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Путь к файлу, формат: (media)/avatar/user_id/photo.jpg"""
    return f"avatar/user_{instance.id}/{file}"


def get_path_upload_image(instance, file):
    """Путь к файлу, формат: (media)/image/user_id/photo.jpg"""
    return f"image/user_{instance.user.id}/{file}"


def get_path_upload_cover_favourite_image(instance, file):
    """Путь к файлу, формат: (media)/favourite/user_id/photo.jpg"""
    return f"favourite/user_{instance.user.id}/{file}"


def validate_size_image(file_obj):
    """Проверка размера файла"""

    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {mb_limit}MB")


def delete_old_file(path_file):
    """Удаление старого файла"""
    if os.path.exists(path_file):
        os.remove(path_file)
