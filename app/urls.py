from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.form, name="form"),
    path("exportar", views.export_csv, name="exportar")
]