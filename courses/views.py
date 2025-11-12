from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "teacher":
            return Course.objects.filter(teacher=user)
        return Course.objects.all()

    def perform_create(self, serializer):
        if self.request.user.role != "teacher":
            raise PermissionError("Only teachers can create courses.")
        serializer.save(teacher=self.request.user)


class EnrollmentView(generics.CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "student":
            raise PermissionError("Only students can enroll in courses.")
        serializer.save(student=self.request.user)


class MyCoursesView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role != "student":
            return Enrollment.objects.none()
        return Enrollment.objects.filter(student=user)
