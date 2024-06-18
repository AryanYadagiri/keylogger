from django.urls import path
from . import views

urlpatterns = [
    path("receive", views.receive_files, name="receive"),
    path("checker", views.checker, name="checker"),
    path("download/<str:file_name>/", views.download, name="download"),
]
