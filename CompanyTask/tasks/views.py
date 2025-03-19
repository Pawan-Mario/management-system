import csv
from django.http import HttpResponse
from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Requires login
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['priority', 'status', 'due_date']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Requires login

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class ExportTasksCSVView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # ✅ Secure API

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

        writer = csv.writer(response)
        writer.writerow(["Title", "Description", "Priority", "Status", "Due Date", "Created At"])

        for task in tasks:
            writer.writerow([task.title, task.description, task.priority, task.status, task.due_date, task.created_at])

        return response
