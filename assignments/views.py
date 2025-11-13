from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer


class AssignmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "teacher":
            return Assignment.objects.filter(course__teacher=user)
        elif user.role == "student":
            return Assignment.objects.filter(course__enrollments__student=user)
        return Assignment.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != "teacher":
            raise PermissionError("Only teachers can create assignments.")
        serializer.save()


class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "student":
            raise PermissionError("Only students can submit assignments.")
        serializer.save(student=self.request.user)


class SubmissionListView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        assignment_id = self.kwargs.get("assignment_id")
        if user.role == "teacher":
            return Submission.objects.filter(assignment__id=assignment_id, assignment__course__teacher=user)
        elif user.role == "student":
            return Submission.objects.filter(assignment__id=assignment_id, student=user)
        return Submission.objects.none()


class GradeSubmissionView(generics.UpdateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        submission = self.get_object()
        if request.user.role != "teacher" or submission.assignment.course.teacher != request.user:
            return Response({"error": "Only the course teacher can grade this submission."},
                            status=status.HTTP_403_FORBIDDEN)

        submission.grade = request.data.get("grade")
        submission.feedback = request.data.get("feedback", "")
        submission.save()
        return Response(SubmissionSerializer(submission).data)
