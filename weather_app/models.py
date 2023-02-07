from django.db import models

# Create your models here.
from django.db import models

#cityweather model will store our weather data from openweather API

class CityWeather(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

#there will be no models for user as django saves our user data automatically.