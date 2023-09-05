from django.urls import path
from api.api import UserApiView

urlpatterns=[
    path('usuario-api/', UserApiView.as_view(), name='usuario_api'),
]