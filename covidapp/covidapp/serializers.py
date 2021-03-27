from rest_framework.serializers import ModelSerializer
from covidapp.covidapp.models import User, Age, Sex, Loc

class UserSerializer(ModelSerializer):
    def create(self, data):
        user= User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = "__all__"

class AgeSerializer(ModelSerializer):
    class Meta:
        model = Age
        fields = "__all__"

class SexSerializer(ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"

class LocSerializer(ModelSerializer):
    class Meta:
        model = Loc
        fields = "__all__"


