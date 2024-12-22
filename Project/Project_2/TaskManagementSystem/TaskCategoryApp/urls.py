from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskCategory, name='taskCategory')
]
