from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name="app"),
    path("test/<str:slug>", views.test, name="test")

    # path("admin/", views, name="admin_panel")
]
