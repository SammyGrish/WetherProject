from rest_framework import serializers
from . import models

class TemperatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','celesius','change','recorded_time',)
        model= models.Temperature