from django.urls import path
from . import views
urlpatterns = [
    path('djangoform/', views.djangoform, name='djangoform')
]
