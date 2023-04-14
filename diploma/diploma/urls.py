#from django.contrib import views
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cbApp/', include('cbApp.urls'), name='cbApp'),
]
