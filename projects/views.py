from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        🔹 Sadece giriş yapan kullanıcının projelerini döndür.
        Eğer herkesinkini göstermek istersen .all()'ı koruyabilirsin.
        """
        return Project.objects.filter(owner=self.request.user).prefetch_related("tasks")

    def perform_create(self, serializer):
        """
        🔹 Yeni proje oluşturulurken owner’ı otomatik olarak giriş yapan kullanıcıya ata.
        """
        serializer.save(owner=self.request.user)
