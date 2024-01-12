from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Department
        fields = '__all__'
        description = "Department ข้อมูลแผนก"

class DepartmentListView(generics.ListCreateAPIView):
    queryset =Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer