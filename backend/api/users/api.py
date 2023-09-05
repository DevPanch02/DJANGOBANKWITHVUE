from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.users.serializer import UserSerializer, ListUserSerializer 

from users.models import User

@api_view(['GET','POST']) 
def UserApiView(request):

    #  LIST
    if request.method=='GET':
        users=User.objects.all().values('id','username','email','password','name')
        userSerializer = ListUserSerializer(users, many=True)
        return Response(userSerializer.data, status=status.HTTP_200_OK)
    
    #   CREATE
    elif request.method=='POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def UserApiDetail(request,pk=None):

#   QUERY ALL   
    user = User.objects.filter(id=pk).first()

    if user:

        #   LIST DETAIL
        if request.method=='GET':
            user_serializer=UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        #   EDIT DETAIL USER
        elif request.method=='PUT':
            user_serializer=UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #   DELETE DETAIL USER
        elif request.method =='DELETE':
            user.delete()
            return Response({'message':'Usuario elimnado'}, status=status.HTTP_200_OK)
        
    return Response({'message':'Usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)





# class UserApiView(APIView):
    
    # def get(self,request):
    #     users=User.objects.all()
    #     userSerializer = UserSerializer(users, many=True)
    #     return Response(userSerializer.data)