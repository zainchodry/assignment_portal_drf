from rest_framework import serializers
from .models import Course, Enrollment
from accounts.models import User


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="teacher.username", read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "teacher", "teacher_name", "created_at"]
        read_only_fields = ["teacher", "created_at"]


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)
    student_name = serializers.CharField(source="student.username", read_only=True)

    class Meta:
        model = Enrollment
        fields = ["id", "student", "student_name", "course", "course_title", "enrolled_at"]
        read_only_fields = ["enrolled_at"]
