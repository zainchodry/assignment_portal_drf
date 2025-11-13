from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serilaizers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class MarkAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"error": "You can only mark your own notifications as read."},
                            status=status.HTTP_403_FORBIDDEN)
        notification.is_read = True
        notification.save()
        return Response(NotificationSerializer(notification).data)
