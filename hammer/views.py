from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PhoneSerializer, VerifySerializer, UserListSerializer
from .models import User
import time

class SendCodeView(APIView):
    def post(self, request):
        time.sleep(1)  # имитация задержки
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response({"message": "Code sent", "code": data['code']})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    def post(self, request):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "User verified"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)