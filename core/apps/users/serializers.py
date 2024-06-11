from rest_framework.serializers import ModelSerializer, CharField

from core.apps.users.models import CustomUser


class CustomUserCommonSerializer(ModelSerializer):
    firstName = CharField(source="first_name")
    lastName = CharField(source="last_name")

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "firstName",
            "lastName",
            "icon",
        )
