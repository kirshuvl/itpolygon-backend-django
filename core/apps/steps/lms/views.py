from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.apps.steps.lms.serializers import (
    UserStepEnrollCreateSerializer,
    UserStepEnrollRetrieveSerializer,
)


@extend_schema(
    tags=["LMS"],
    summary="UserStepEnrolls Create",
)
class UserStepEnrollCreateAPIView(CreateAPIView):
    serializer_class = UserStepEnrollCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            UserStepEnrollRetrieveSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )
