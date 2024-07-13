from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('exercises/', views.exercise_list),
    path('exercises/<int:id>/', views.exercise_detail)
]