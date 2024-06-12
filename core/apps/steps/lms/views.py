from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from core.apps.steps.models import UserStepEnroll

from core.apps.steps.lms.serializers import (
    UserStepEnrollCreateSerializer,
    UserStepEnrollRetrieveSerializer,
)


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepEnrolls Create",
)
class UserStepEnrollCreateAPIView(CreateAPIView):
    serializer_class = UserStepEnrollCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            instance = UserStepEnroll.objects.get(user=self.request.user, step=request.data["step"])
            serializer = UserStepEnrollRetrieveSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserStepEnroll.DoesNotExist:
            pass

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            UserStepEnrollRetrieveSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    tags=["LMS", "Step"],
    summary="UserStepEnrolls Update",
)
class UserStepEnrollsUpdateAPIVIew(RetrieveAPIView, UpdateAPIView):
    serializer_class = UserStepEnrollRetrieveSerializer
    lookup_url_kwarg = "enrollId"
    http_method_names = ["patch"]

    def get_queryset(self):
        return UserStepEnroll.objects.all()
