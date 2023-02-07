from django.contrib import admin
from .models import CityWeather
# Register your models here.
#this CityWeather will show in our admin panel.


admin.site.register(CityWeather)