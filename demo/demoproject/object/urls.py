from django.urls import path

from demoproject.object import views

app_name = "object"
urlpatterns = [
    path(
        "default-file/<slug:slug>/",
        views.default_file_view,
        name="default_file",
    ),
    path(
        "another-file/<slug:slug>/",
        views.another_file_view,
        name="another_file",
    ),
    path(
        "deserialized_basename/<slug:slug>/",
        views.deserialized_basename_view,
        name="deserialized_basename"
    ),
    path(
        "inline-file/<slug:slug>/",
        views.inline_file_view,
        name="inline_file",
    ),
]

