from django.db import models
from django.conf import settings
from courses.models import Course
from accounts.models import User


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("assignment", "student")

    def __str__(self):
        return f"{self.student.username} → {self.assignment.title}"
