from django.urls import path
from .views import UserView

app_name = 'covidapp'
urlpatterns = [
    path('user/', UserView.as_view(), name='users'),
]