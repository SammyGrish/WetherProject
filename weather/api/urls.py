from django.urls import path

from . import views

urlpatterns = [
    path('T', views.TemperatureList.as_view()),
    path('T/<int:pk>/', views.TemperatureDetail.as_view()),
    path('H', views.HumidityList.as_view()),
    path('H/<int:pk>/', views.HumidityDetail.as_view()),
    path('P', views.PressureList.as_view()),
    path('P/<int:pk>/', views.PressureDetail.as_view()),
    
]