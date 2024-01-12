from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta : 
        model = Company
        fields = '__all__'


class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer