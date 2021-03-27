from rest_framework.serializers import ModelSerializer
from .models import UserInfo, Age, Sex, Loc
deom django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(ModelSerializer):
    def create(self, data):
        user= User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        )
        validators = [
            UniqueTogetherValidator(
                queryset = User.objects.all()
                fields=['username','email']
            )
        ]

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class AgeSerializer(ModelSerializer):
    class Meta:
        model = Age
        fields = '__all__'

class SexSerializer(ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'

class LocSerializer(ModelSerializer):
    class Meta:
        model = Loc
        fields = '__all__'


