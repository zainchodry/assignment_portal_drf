from rest_framework import serializers
from .models import Assignment, Submission


class AssignmentSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course.title", read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "title", "description", "due_date", "course", "course_name", "created_at"]
        read_only_fields = ["created_at"]


class SubmissionSerializer(serializers.ModelSerializer):
    assignment_title = serializers.CharField(source="assignment.title", read_only=True)
    student_name = serializers.CharField(source="student.username", read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "assignment",
            "assignment_title",
            "student",
            "student_name",
            "file",
            "submitted_at",
            "grade",
            "feedback",
        ]
        read_only_fields = ["submitted_at", "grade", "feedback", "student"]
