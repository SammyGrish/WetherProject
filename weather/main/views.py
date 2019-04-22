from django.shortcuts import render
from api.models import Temperature
from api.models import Humidity
from api.models import Pressure

def home(request):
    temp =   Temperature.objects.order_by('-recorded_time').first()
    tcount = Temperature.objects.count()
    tfirst = Temperature.objects.order_by('recorded_time').first()
    humidity = Humidity.objects.order_by('-recorded_time').first()
    hcount = Humidity.objects.count()
    hfirst = Humidity.objects.order_by('recorded_time').first()
    pressure = Pressure.objects.order_by('-recorded_time').first()
    pcount = Pressure.objects.count()
    pfirst = Pressure.objects.order_by('recorded_time').first()
    return render(request, 'home.html', {
        'temp': temp,
        'tcount': tcount, 
        'tfirst': tfirst.recorded_time,
        'humidity': humidity,
        'hcount': hcount,
        'hfirst': hfirst.recorded_time,
        'pressure': pressure,
        'pcount': pcount,
        'pfirst': pfirst.recorded_time,
    }
    )
