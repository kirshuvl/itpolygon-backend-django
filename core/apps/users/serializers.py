from core.apps.users.models import CustomUser

from rest_framework.serializers import CharField, ModelSerializer


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
