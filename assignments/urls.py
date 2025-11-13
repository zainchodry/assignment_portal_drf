from django.urls import path
from .views import (
    AssignmentListCreateView,
    SubmissionCreateView,
    SubmissionListView,
    GradeSubmissionView,
)

urlpatterns = [
    path("assignments/", AssignmentListCreateView.as_view(), name="assignment-list-create"),
    path("submissions/", SubmissionCreateView.as_view(), name="submission-create"),
    path("submissions/<int:assignment_id>/", SubmissionListView.as_view(), name="submission-list"),
    path("grade/<int:pk>/", GradeSubmissionView.as_view(), name="grade-submission"),
]
