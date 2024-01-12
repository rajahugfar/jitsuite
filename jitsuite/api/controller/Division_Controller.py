from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Division

class DivisionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Division
        fields = '__all__'
        description = "Division หน่วยงาน"

class DivisionView(generics.ListCreateAPIView):
    queryset =Division.objects.all()
    serializer_class = DivisionSerializer

class DivisionDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer