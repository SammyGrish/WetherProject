from django.shortcuts import render
from api.models import Temperature


def home(request):
    temp =   Temperature.objects.order_by('-recorded_time').first()
    tcount = Temperature.objects.count()
    tfirst = Temperature.objects.order_by('recorded_time').first()
    
    return render(request, 'home.html', {
        'temp': temp,
         'tcount': tcount, 
         'tfirst': tfirst.recorded_time}
    )
