from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path('test', views.test, name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
