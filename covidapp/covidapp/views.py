from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, Age, Sex, Loc
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserInfoSerializer, AgeSerializer, SexSerializer, LocSerializer
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
    def get(self, format=None):
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(data=request.data, request=request)
            return Response(
                serializer.data
            )
        return Response(
            {
                'error': True,
                'error_msg': serializer.error_messages,
            }
        )

class RiskView(APIView):      
    def get(self, request, format=None):
        c = connection.cursor()
        c.execute("SELECT * FROM covidapp_userinfo WHERE user_id = " + str(request.user.id) + ";")
        user = c.fetchall()
        location = request.data.get('location')
        c.execute("SELECT prob FROM covidapp_age WHERE covidapp_age.age_max = " + str(user[1]) + ";")
        ageprob = c.fetchall()
        c.execute("SELECT prob FROM covidapp_sex WHERE covidapp_sex.sex = " + str(user[2]) + ";")
        sexprob = c.fetchall()
        c.execute("SELECT risk, outbreak FROM covidapp_loc WHERE covidapp_loc.name = " + str(location) + ";")
        locinfo = c.fetchall()
        locrisk = locinfo[0] #maybe [0][0]
        locout = locinfo[1] #maybe [0][1]
        risk = 0
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
