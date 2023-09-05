from rest_framework import serializers

# from backend.users.models import User

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'