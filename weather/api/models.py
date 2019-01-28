from django.db import models


class temperature(models.Model):
    celesius = models.FloatField(default=0.0)
    change = models.FloatField(default =0.0)                                
    
class Humitidty(models.Model):
    pass