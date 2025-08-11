from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()
    Serializer = TaskSerializer(instance=tasks, many=True)
    return Response(Serializer.data)

@api_view(['GET'])
def retrieve_task(request, task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskSerializer(instance=task)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
