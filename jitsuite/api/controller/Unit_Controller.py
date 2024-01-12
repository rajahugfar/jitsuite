from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Unit
        fields = '__all__'
        description = "Unit ข้อมูลหน่วยงาน"

class UnitListView(generics.ListCreateAPIView):
    queryset =Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer