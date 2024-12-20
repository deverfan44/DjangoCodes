from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_profile, name='add_profile'),
]