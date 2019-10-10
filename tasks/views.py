from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin):
    queryset = Task.objects.select_related('user')
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
