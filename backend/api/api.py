from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import UserSerializer
from users.models import User

class UserApiView(APIView):
    
    def get(self,request):
        users=User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return Response(userSerializer.data)