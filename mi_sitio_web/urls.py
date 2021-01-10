# mi_sitio_web/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
  url('admin/', admin.site.urls),
  url('', include('mi_aplicacion.urls')),
  path('accounts/', include('allauth.urls')),
]