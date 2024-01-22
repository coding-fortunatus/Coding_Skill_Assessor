from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.app, name="app"),
    path("test/<str:slug>/<int:question_num>/", views.test, name="test"),
    # path("submission", views.submission, name="submission")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
