from django.urls import path
from .views import *

urlpatterns = [
    path('',get_tasks, name='get_tasks'),
    path('<int:task_id>/',get_task, name='get_tasks'),
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/update/', update_task, name='update_task'),
    path('<int:task_id>/partial_update/', partial_update_task, name='partial_update_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
]