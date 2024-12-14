from django.urls import path
from . import views

urlpatterns = [
    path('djangoform/', views.djangoform, name='djangoform'),
    path('studentform/', views.stdform, name='stdform'),
    path('passwordform/', views.passwordValidation, name='passwordform')
]
