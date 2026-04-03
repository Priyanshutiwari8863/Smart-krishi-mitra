from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_list, name='crop_list'),
    path('market/', views.market, name='market'),
]