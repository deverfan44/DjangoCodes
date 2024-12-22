from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskModel, name='taskModel'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task')
]
