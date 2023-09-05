from rest_framework import serializers

# from backend.users.models import User

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

#   PARA ENCRIPTAR EL PASSWORD
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    #   ACTULIZAR A PASSWORD ENCRIPTADO
    def update(self, instance, validated_data):
        update_user= super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
    


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

    # FUNCIONAMIENTO SOLO CUANDO SE USE VALUE EN LA FUNCION
    def to_representation(self, instance):
        return {
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password'],
        }