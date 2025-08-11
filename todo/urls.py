from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/',list_tasks, name='list_tasks'),
    path('tasks/<int:task_id>/', retrieve_task, name='retrieve_task'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:task_id>/update/', update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
]