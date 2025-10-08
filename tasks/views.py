from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tasks.
    Allows authenticated users to list, create, update and delete tasks.
    Supports partial updates (PATCH) for updating task status.
    """
    queryset = Task.objects.all().select_related('project')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.all().select_related('project')

    def perform_create(self, serializer):
        # Kaydı doğrudan oluştur
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        """
        Handles PATCH updates for task status or any single field.
        """
        kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
