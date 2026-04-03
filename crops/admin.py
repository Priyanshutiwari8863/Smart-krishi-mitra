from django.contrib import admin
from .models import Crop
from .models import MarketPrice
# Register your models here.
admin.site.register(Crop)


admin.site.register(MarketPrice)