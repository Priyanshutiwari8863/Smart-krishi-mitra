from django.shortcuts import render
from .models import DetectionHistory
import requests

def history(request):

    data = DetectionHistory.objects.filter(
        user=request.user
    ).order_by('-date')

    return render(request,'history.html',{
        'history': data
    })



