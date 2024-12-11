from django.urls import path
from . import views

urlpatterns = [
    path('', views.djangoForm, name='django_form')
]
