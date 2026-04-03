from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from crops import views as crop_views   # 👈 add this


# Home page
def home(request):
    return render(request, 'home.html')


urlpatterns = [
    
    path('', home, name='home'),

    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),
    path('crops/', include('crops.urls')),
    path('ai/', include('ai_engine.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('history/', include('history.urls')),

    # Market
    path('market/', crop_views.market, name='market'),

    # Products
    path('', include('products.urls')),
    path('weather/', include('weather.urls')),
     path('schemes/', include('schemes.urls')),  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)