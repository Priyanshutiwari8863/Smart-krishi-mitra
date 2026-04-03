from django.shortcuts import render


# Create your views here.
from products.models import Disease, Medicine, Product
from django.core.files.storage import FileSystemStorage
from .plant_disease_model import predict_plant_disease

from .models import Shop


def disease(request):

    disease_data = None
    medicines = None
    products = None

    if request.method == "POST":

        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        # AI prediction
        detected_disease = predict_plant_disease(filename)

        # Get disease from DB
        disease_data = Disease.objects.filter(
            disease_name=detected_disease
        ).first()

        # Get medicines
        medicines = Medicine.objects.filter(disease__disease_name=detected_disease)

        # Get products
        products = Product.objects.all()

    context = {
        'disease': disease_data,
        'medicines': medicines,
        'products': products
    }

    return render(request, 'ai_engine/disease.html', context)







def shops(request):
    shops = Shop.objects.all()
    return render(request,'products/shops.html',{
        'shops':shops
    })