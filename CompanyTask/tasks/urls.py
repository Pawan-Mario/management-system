from django.urls import path
from .views import TaskListCreateView, TaskDetailView, ExportTasksCSVView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),  # ✅ Create & List Tasks
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # ✅ Update & Delete Tasks
    path('tasks/export/', ExportTasksCSVView.as_view(), name='task-export'),  # ✅ Export Tasks as CSV
]
