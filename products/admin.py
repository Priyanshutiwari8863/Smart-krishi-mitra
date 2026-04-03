from django.contrib import admin
from .models import Disease, Medicine, Product
from .models import Scheme,Shop
# Register your models here.
admin.site.register(Medicine)
admin.site.register(Product)
admin.site.register(Disease)
admin.site.register(Scheme)
admin.site.register(Shop)