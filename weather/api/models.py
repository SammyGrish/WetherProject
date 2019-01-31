from django.db import models


class Temperature(models.Model):
    celesius = models.FloatField(default=0.0)
    change = models.FloatField(default =0.0)
    recorded_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.celesius)
    
class Humitidty(models.Model):
    pass