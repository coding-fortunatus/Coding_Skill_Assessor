from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("users", views.allUser, name="users"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
