from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid


#Registrationapi for user to register
class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import CityWeather
from .serializers import CityWeatherSerializer

#weatherapi view to change our data in our data base to JSON format
class WeatherInformationAPIView(generics.ListAPIView):
    queryset = CityWeather.objects.all()
    serializer_class = CityWeatherSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        return self.queryset.all()

import requests

#fetch_weather_data view function is used to fetch data from openweather using API KEY
def fetch_weather_data(city):
    API_KEY = '256be8862a53a742dab9658634ccb6f2'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

#these are the 30 cities. weather report of these 30 cities report will be fetched and saved in our DB.

cities = ['London', 'Paris', 'Berlin', 'Madrid', 'Rome', 'Moscow', 'Istanbul', 'Beijing', 'Tokyo', 'Shanghai','Mumbai', 'Delhi', 'Bangkok', 'Jakarta', 'Seoul', 'Manila', 'Singapore', 'Taipei', 'Sydney', 'Melbourne','Los Angeles', 'New York', 'Toronto', 'Mexico City', 'São Paulo', 'Rio de Janeiro', 'Buenos Aires','Lima', 'Caracas','madurai']
for city in cities:
    weather_data = fetch_weather_data(city)
    if 'main' in weather_data:
        city_weather = CityWeather(
            city_name=city,
            temperature=weather_data['main']['temp'],
            pressure=weather_data['main']['pressure'],
            humidity=weather_data['main']['humidity'],
            description=weather_data['weather'][0]['description']
        )
        city_weather.save()
    else:
        print(f"No weather data found for {city}")

