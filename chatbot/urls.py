from django.urls import path
from . import views

urlpatterns = [

    # Chatbot page
    path('', views.chatbot, name='chatbot'),
    path('voice/',views.voice_assistant,name='voice'),

]