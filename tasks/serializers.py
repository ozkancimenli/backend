from rest_framework import serializers
from .models import Task
from projects.models import Project


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        required=True
    )

    class Meta:
        model = Task
        fields = '__all__'
        ref_name = 'TaskSerializer'
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': False},
            'status': {'required': False},
            'due_date': {'required': False},
        }

    def update(self, instance, validated_data):
        # Partial update destekli (sadece gelen alanları günceller)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
