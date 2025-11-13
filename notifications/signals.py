from django.db.models.signals import post_save
from django.dispatch import receiver
from assignments.models import Assignment, Submission
from .models import Notification
from courses.models import Enrollment


@receiver(post_save, sender=Assignment)
def notify_students_on_assignment(sender, instance, created, **kwargs):
    if created:
        enrolled_students = Enrollment.objects.filter(course=instance.course)
        for enrollment in enrolled_students:
            Notification.objects.create(
                recipient=enrollment.student,
                title="New Assignment Posted",
                message=f"A new assignment '{instance.title}' was added to the course '{instance.course.title}'.",
            )


@receiver(post_save, sender=Submission)
def notify_teacher_on_submission(sender, instance, created, **kwargs):
    if created:
        teacher = instance.assignment.course.teacher
        Notification.objects.create(
            recipient=teacher,
            title="New Submission Received",
            message=f"{instance.student.username} submitted '{instance.assignment.title}'.",
        )


@receiver(post_save, sender=Submission)
def notify_student_on_grading(sender, instance, created, **kwargs):
    if not created and instance.grade is not None:
        Notification.objects.create(
            recipient=instance.student,
            title="Assignment Graded",
            message=f"Your submission for '{instance.assignment.title}' was graded. Grade: {instance.grade}",
        )
