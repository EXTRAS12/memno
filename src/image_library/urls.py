from django.urls import path

from . import views

urlpatterns = [
    path("", views.ImageView.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        views.ImageView.as_view({"put": "update", "delete": "destroy"}),
    ),
    path("list/", views.ImageListView.as_view()),
    path("author-image-list/<int:pk>/", views.AuthorImageListView.as_view()),
    path("stream-image/<int:pk>/", views.StreamImageView.as_view()),
    path(
        "comments/",
        views.CommentAuthorView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "comments/<int:pk>/",
        views.CommentAuthorView.as_view(
            {"put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "comments_by_image/<int:pk>/",
        views.CommentView.as_view({"get": "list"}),
    ),
    path("download-image/<int:pk>/", views.DownloadImageView.as_view()),
    path(
        "favourite/",
        views.FavouriteImageListView.as_view(
            {"get": "list", "post": "create"}
        ),
    ),
    path(
        "favourite/<int:pk>/",
        views.FavouriteImageListView.as_view(
            {"put": "update", "delete": "destroy"}
        ),
    ),
]
