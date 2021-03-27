from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, Age, Sex, Loc
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserInfo, AgeSerializer, SexSerializer, LocSerializer
# Create your views here.
class UserView(APIView):
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'error': True,
                'error_msg': serializer.error_messages,
            }
        )
        status=status.HTTP_400_BAD_REQUEST

class AgeView(APIView):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer

class SexView(APIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class LocView(APIView):
    queryset = Loc.objects.all()
    serializer_class = LocSerializer
