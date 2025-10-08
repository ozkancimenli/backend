from rest_framework import serializers
from .models import Project
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "due_date",
            "created_at",
        ]
        ref_name = "ProjectTaskSerializer"  # 🔹 Çakışmayı önler


class ProjectSerializer(serializers.ModelSerializer):
    # 🔹 Tasks read-only olarak nested geliyor (frontend’te listede görünüyor)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_at", "tasks"]
