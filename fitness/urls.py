from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('sessions/', views.session_list),
    path('sessions/<int:id>/', views.session_detail)
]