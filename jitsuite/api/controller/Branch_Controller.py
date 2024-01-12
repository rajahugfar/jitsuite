from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta :
        model = Branch
        fields = '__all__'
        description = "Branch ข้อมูลสาขา"

class BranchView(generics.ListCreateAPIView):
    queryset =Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer