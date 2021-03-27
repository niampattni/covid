from django.shortcuts import render
#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Age, Sex, Loc
from .serializers import UserSerializer, AgeSerializer, SexSerializer, LocSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
#    def post(self, request):
#        serializer = UserSerializer(data=request.data)
#        if serializer.is_valid(raise_exception=ValueError):
#            serializer.create(data=request.data)
#            return Response(
#                serializer.data,
#                status=status.HTTP_201_CREATED
#            )
#        return Response(
#            {
#                'error': True,
#                'error_msg': serializer.error_messages,
#            },
#            status=status.HTTP_400_BAD_REQUEST
#        )
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgeViewSet(viewsets.ModelViewSet):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer

class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class LocViewSet(viewsets.ModelViewSet):
    queryset = Loc.objects.all()
    serializer_class = LocSerializer
