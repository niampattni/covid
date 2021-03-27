from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, Age, Sex, Loc
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserInfo, AgeSerializer, SexSerializer, LocSerializer
from django.db import connection
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

class InfoView(APIView):
    def post(self, request):
        c = connection.cursor()
        age = request.data.get('age')
        sex = request.data.get('sex')
        id = request.user.id
        c.execute("INSERT INTO covidapp_userinfo (age, sex, user_id) VALUES (" + str(age) + ", " + str(sex) + ", " + str(id) + ");")

class RiskView(APIView):
    def get(seld, request, format=None):
        c = connection.cursor()
        c.execute("SELECT * FROM covidapp_userinfo WHERE user_id = " + str(request.user.id) + ";")
        c.fetchall()
        location = request.data.get('location')
        #perform risk calculation here and return json response
        return Response(risk)

class AgeView(APIView):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer

class SexView(APIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class LocView(APIView):
    queryset = Loc.objects.all()
    serializer_class = LocSerializer
