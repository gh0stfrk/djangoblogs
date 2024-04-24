from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("create-post/", views.create_post, name="create_post"),
    path("update-post/<int:pk>/", views.update_post, name="update_post"),
    path("detail/<int:pk>/", views.post_detail, name="detail"),
    path("like", views.like_a_post, name="like"),
    path("comment", views.add_comment, name="comment")
]
