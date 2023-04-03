from cbApp import views
from django.urls import path
urlpatterns = [
    path('ALLProducts/', views.getALLProducts)
]