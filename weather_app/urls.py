from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from weather_app.views import RegistrationAPIView , WeatherInformationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
    path('weather-info/', WeatherInformationAPIView.as_view(), name='weather_info'),

]
