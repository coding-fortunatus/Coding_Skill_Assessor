from django.contrib import admin
from django.urls import path, include
# from home.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('app/', include('dashboard.urls'))
]
