from django.urls import path

from core.apps.steps.lms.views import (
    UserAnswerForProblemStepCreateAPIView,
    UserAnswerForQuestionStepCreateAPIView,
    UserAnswerForSingleChoiceQuestionStepCreateAPIView,
    UserStepBookmarkCreateAPIView,
    UserStepBookmarkDeleteAPIView,
    UserStepEnrollCreateAPIView,
    UserStepEnrollsUpdateAPIVIew,
    UserStepLikeCreateAPIView,
    UserStepLikeDeleteAPIView,
    UserStepViewCreateAPIView,
)

urlpatterns = [
    path(
        "steps/enrolls/",
        UserStepEnrollCreateAPIView.as_view(),
    ),
    path(
        "steps/enrolls/<int:enrollId>/",
        UserStepEnrollsUpdateAPIVIew.as_view(),
    ),
    path(
        "steps/likes/",
        UserStepLikeCreateAPIView.as_view(),
    ),
    path(
        "steps/likes/<int:likeId>/",
        UserStepLikeDeleteAPIView.as_view(),
    ),
    path(
        "steps/bookmarks/",
        UserStepBookmarkCreateAPIView.as_view(),
    ),
    path(
        "steps/bookmarks/<int:bookmarkId>/",
        UserStepBookmarkDeleteAPIView.as_view(),
    ),
    path(
        "steps/views/",
        UserStepViewCreateAPIView.as_view(),
    ),
    path(
        "steps/answers/",
        UserAnswerForQuestionStepCreateAPIView.as_view(),
    ),
    path(
        "steps/answers/single/",
        UserAnswerForSingleChoiceQuestionStepCreateAPIView.as_view(),
    ),
    path(
        "steps/codes/",
        UserAnswerForProblemStepCreateAPIView.as_view(),
    ),
]
