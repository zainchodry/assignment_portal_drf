from django.urls import path
from .views import CourseListCreateView, EnrollmentView, MyCoursesView

urlpatterns = [
    path("courses/", CourseListCreateView.as_view(), name="course-list-create"),
    path("enroll/", EnrollmentView.as_view(), name="course-enroll"),
    path("my-courses/", MyCoursesView.as_view(), name="my-courses"),
]
