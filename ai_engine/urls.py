from django.urls import path
from . import views

urlpatterns = [

path('recommend/', views.recommend, name='recommend'),
path('weather/', views.weather, name='weather'),
path('disease/', views.detect_disease, name='disease'),
path('yield/', views.yield_prediction, name='yield'),
path('soil/', views.soil_detection, name='soil'),
path('weather/', views.weather, name='weather'),
]