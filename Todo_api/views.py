from django.shortcuts import render
from Todo.models import TodoModel
from .models import TodoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

class Todoapi(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
    authentication_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]