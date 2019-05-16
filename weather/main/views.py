from django.shortcuts import render
from api.models import Temperature,Humidity,Pressure
from datetime import datetime, timedelta
from django.db.models import Max, Min, F
from chartjs.views.lines import BaseLineChartView
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

class LineChartView(BaseLineChartView):
    type = ''
    labels = []
    max_list = []
    min_list = []
    def set_minmax(self, index, item):
        if item > self.max_list[index]:
            self.max_list[item]=item
        if item < self.min_list[index]:
            self.min_list[item]=item
            
    def last_seven_days(self):
        self.type = self.kwargs.get('type')
        now = datetime.now()
        seven_days_ago = now-timedelta(days=7)
        if self.type== 'rh':
            datas= Humidity.objects.order_by('recorded_time').filter(recorded_time__range=(seven_days_ago,now)).annotate(value=F('RH'))
        elif self.type == 'bp':
            datas = Pressure.objects.order_by('recorded_time').filter(recorded_time__range=(seven_days_ago,now)).annotate(value=F('BP'))
        else:
            datas = Temperature.objects.order_by('recorded_time').filter(recorded_time__range=(seven_days_ago,now)).annotate(value=F('celesius'))
        print(str(data.recorded_time)+'='+str(weekday)+' '+ days[weekday])
        print (datas)
        for data in datas:
            weekday = datetime.weekday(data.recorded_time)
            if days[weekday] not in self.labels:
                self.labels.append(days[weekday])
        self.max_list = [-100 for i in range(len(self.labels))]
        self.min_list = [9999 for i in range(len(self.labels))]
        for data in datas:
            weekday = datetime.weekday(data.recorded_time)
            idx = self.labels.index(days[weekday])
            self.set_minmax(idx, data.value)
    def get_providers(self):
        return['Max','Min']
    def get_labels(self):
        return self.labels
    def get_data(self):
        self.last_seven_days
        
        return[self.max_list,self.min_list]

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
