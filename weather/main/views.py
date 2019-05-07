from django.shortcuts import render
from api.models import Temperature
from api.models import Humidity
from api.models import Pressure
from datetime import datetime, timedelta
from django.db.models import Max, Min

def home(request):
    now = datetime.now()
    Atime_ago = now - timedelta(days=7)
    temp =   Temperature.objects.order_by('-recorded_time').first()
    tcount = Temperature.objects.count()
    tfirst = Temperature.objects.order_by('recorded_time').first()
    tmax = Temperature.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Max('celesius'))['celesius__max']
    tmin = Temperature.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Min('celesius'))['celesius__min']
    humidity = Humidity.objects.order_by('-recorded_time').first()
    hcount = Humidity.objects.count()
    hfirst = Humidity.objects.order_by('recorded_time').first()
    hmax = Humidity.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Max('RH'))['RH__max']
    hmin = Humidity.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Min('RH'))['RH__min']
    pressure = Pressure.objects.order_by('-recorded_time').first()
    pcount = Pressure.objects.count()
    pfirst = Pressure.objects.order_by('recorded_time').first()
    pmax = Pressure.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Max('BP'))['BP__max']
    pmin = Pressure.objects.filter(
        recorded_time__range=(Atime_ago,now)
        ).aggregate(Min('BP'))['BP__min']
    return render(request, 'home.html', {
        'temp': temp,
        'tcount': tcount, 
        'tfirst': tfirst.recorded_time,
        'tmax':tmax,
        'tmin':tmin,
        'humidity': humidity,
        'hcount': hcount,
        'hfirst': hfirst.recorded_time,
        'hmax':hmax,
        'hmin':hmin,
        'pressure': pressure,
        'pcount': pcount,
        'pfirst': pfirst.recorded_time,
        'pmax':pmax,
        'pmin':pmin,
    }
    )
