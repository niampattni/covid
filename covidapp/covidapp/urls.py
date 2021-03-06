from django.urls import path
from .views import UserView, InfoView, RiskView, LogoutView

app_name = 'covidapp'
urlpatterns = [
    path('login/', UserView.as_view(), name='login'),
    path('info/', InfoView.as_view(), name='info'),
    path('risk/', RiskView.as_view(), name='risk'),
    path('logout/', LogoutView.as_view(), name='logout')
]