from django.urls import path
from . import views

urlpatterns = [
    path('picture/', views.gallaryPage, name = 'gallaryPage'),
    path('about/', views.about, name = 'aboutPage'),
    path('bootstrap/<int:id>/', views.bootstarpLink, name = 'bootstrap'),
]
