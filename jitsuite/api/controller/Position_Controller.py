from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Position
        fields = '__all__'
        description = "Position ตำแหน่ง"

class PositionView(generics.ListCreateAPIView):
    queryset =Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer