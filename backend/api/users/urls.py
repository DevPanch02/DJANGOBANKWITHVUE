from django.urls import path
from api.users.api import UserApiView, UserApiDetail


urlpatterns=[
    path('usuario-api/', UserApiView, name='usuario_api'),
    path('usuario-api/<int:pk>/', UserApiDetail, name='usuario_detail_api'),
]