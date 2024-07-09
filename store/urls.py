from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail)
]