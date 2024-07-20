from django.urls import path
from . import views



urlpatterns = [
path("post/<int:id>", views.post_handle, name='post_handle' ),
path("post/create", views.post_create, name='post_create'),
path("post/<int:id>/delete", views.post_delete, name='post_delete'),
path("post/<int:id>/edit", views.post_edit, name='post_edit'),
]