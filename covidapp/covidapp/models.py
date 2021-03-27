from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfo(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Age(models.Model):
    age_max = models.IntegerField()
    prob = models.DecimalField(max_digits=4,decimal_places=2)

class Sex(models.Model):
    sex = models.CharField(max_length=1)
    prob = models.DecimalField(max_digits=4,decimal_places=2)
    age_group = models.ForeignKey(Age, on_delete=models.CASCADE)

class Loc(models.Model):
    name = models.CharField(max_length=30)
    risk = models.DecimalField(max_digits=4,decimal_places=2)
    outbreak = models.DecimalField(max_digits=4,decimal_places=2)
