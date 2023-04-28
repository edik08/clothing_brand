from cbApp import views
from django.urls import path, re_path

urlpatterns = [
    path('ALLProducts/', views.getALLProducts),
    path('Products/create', views.add_product),
    re_path(r'Product/$', views.get_Product_by_id),
    path('Products/update', views.update_Product_data),
    path('order/calculate_material', )
]