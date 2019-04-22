from rest_framework import serializers
from . import models

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','celesius','change','recorded_time',)
        model= models.Temperature
class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','RH','change','recorded_time',)
        model= models.Humidity
    
class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','BP','change','recorded_time',)
        model= models.Pressure
        
        