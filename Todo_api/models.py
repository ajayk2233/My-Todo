from django.db import models
from Todo.models import TodoModel
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'