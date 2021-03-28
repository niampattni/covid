from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, Age, Sex, Loc
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserInfoSerializer, AgeSerializer, SexSerializer, LocSerializer
from django.db import connection
from decimal import *
# Create your views here.
class UserView(APIView):    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
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
    def post(self, request):
        user = UserInfo.objects.get(user_id=str(request.user.id))
        agegroup = user.age // 10
        if agegroup == 0:
            agegroup += 1
        ageprob = Age.objects.get(id=agegroup).prob
        ageprob /= 100
        sexprob = Sex.objects.get(age_group_id=agegroup, sex=user.sex).prob
        sexprob /= 100
        exp = request.data.get('exp')
        exp = (0.25 * (1 - pow(0.953, exp))) / (1 - 0.953)
        expfac = Decimal(str(exp))
        locfac = Loc.objects.get(category=str(request.data.get('location'))).risk
        if expfac == 0:
            expfac += 1
        risk = 4 * (((ageprob + sexprob) / locfac) + expfac)
        return Response(risk)

class LogoutView(APIView):
    def get(self, request, format=None):
        if request.user.is_active:
            logout(request)
        return Response("Logged out")

class AgeView(APIView):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer

class SexView(APIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class LocView(APIView):
    queryset = Loc.objects.all()
    serializer_class = LocSerializer
