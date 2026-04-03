from django.urls import path
from . import views

urlpatterns = [
    path('', views.govt_schemes, name='govt_schemes'),
]