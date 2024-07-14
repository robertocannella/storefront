from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('routines/', views.routine_list),
    path('routines/<int:id>/', views.routine_detail)
]