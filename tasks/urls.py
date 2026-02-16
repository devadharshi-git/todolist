# urls.py
from django.urls import path
from .views import home, editTask,deleteTask,addTask

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:task_id>/', editTask, name='edit_task'),
    path('delete/<int:task_id>/', deleteTask, name='delete_task'),
    path('add/', addTask, name='add_task'),

]