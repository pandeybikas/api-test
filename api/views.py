from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializerClass
from .models import StudentAPI
# Create your views here.
class Student_view_base(APIView):
    try:
        def get(self, request, format=None):
            stu = StudentAPI.objects.all()
            serializer= StudentSerializerClass(stu, many=True)
            return Response(serializer.data)
    except Exception as e:
        print("API failed to load", e)