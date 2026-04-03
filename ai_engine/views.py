# Import requests for weather API
import requests

# Import render
from django.shortcuts import render

# Login Required
from django.contrib.auth.decorators import login_required

# Import Crop model
from crops.models import Crop

# File upload
from django.core.files.storage import FileSystemStorage

# Import AI models
from .plant_disease_model import predict_plant_disease
from .yield_model import predict_yield
from .soil_model import detect_soil

# Import Models
from products.models import Disease, Medicine, Product
from history.models import DetectionHistory


# Crop Recommendation View
def recommend(request):

    crop = None
    error = None

    if request.method == "POST":

        soil = request.POST.get('soil')
        season = request.POST.get('season')

        if not soil or not season:
            error = "Please select soil and season"

        else:
            crop = Crop.objects.filter(
                soil_type__iexact=soil,
                season__iexact=season
            ).first()

    return render(request, 'ai_engine/recommend.html', {
        'crop': crop,
        'error': error
    })


# Weather View

def weather(request):

    weather_data = None
    forecast_data = None
    rain_alert = None
    farming_advice = None
    rain_today = None
    rain_week = None
    error = None

    API_KEY = "c4c2829891234580814235307262903"

    if request.method == "POST":

        city = request.POST.get('city')

        url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=7"

        response = requests.get(url)
        data = response.json()

        if "location" in data:

            # Current Weather
            weather_data = {
    'city': data['location']['name'],
    'temperature': data['current']['temp_c'],
    'description': data['current']['condition']['text'],
    'icon': data['current']['condition']['icon'],
    'humidity': data['current']['humidity'],
    'wind': data['current']['wind_kph'],
    'feels': data['current']['feelslike_c'],
    'sunrise': data['forecast']['forecastday'][0]['astro']['sunrise'],
    'sunset': data['forecast']['forecastday'][0]['astro']['sunset'],
    'time': data['location']['localtime']
}
            # Forecast
            forecast_data = data['forecast']['forecastday']

            # Rain Today
            today = data['forecast']['forecastday'][0]
            rain_today = today['day']['daily_chance_of_rain']

            # Rain Week
            rain_week = []

            for day in forecast_data:
                rain_week.append({
                    'date': day['date'],
                    'rain': day['day']['daily_chance_of_rain']
                })

            # Rain Alert + Farming Advice
            if int(rain_today) > 60:
                rain_alert = "🌧 Heavy rain expected today"
                farming_advice = "Avoid irrigation and protect crops"
            elif int(rain_today) > 30:
                rain_alert = "🌦 Possible rain today"
                farming_advice = "Plan irrigation carefully"
            else:
                rain_alert = "☀ No rain expected"
                farming_advice = "Good day for irrigation"

        else:
            error = "Invalid city"

    return render(request, 'ai_engine/weather.html', {
        'weather': weather_data,
        'forecast': forecast_data,
        'rain_alert': rain_alert,
        'farming_advice': farming_advice,
        'rain_today': rain_today,
        'rain_week': rain_week,
        'error': error
    })
# Disease Detection View
@login_required
def detect_disease(request):

    disease_data = None
    medicines = None
    products = None
    error = None
    detected_disease = None

    if request.method == "POST":

        image = request.FILES.get('image')

        if not image:
            error = "Please upload image"
            return render(request,'ai_engine/disease.html',{
                'error': error
            })

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        image_path = fs.path(filename)

        # AI prediction
        prediction = predict_plant_disease(image_path)

        print("Prediction Raw:", prediction)

        detected_disease = str(prediction)
        detected_disease = detected_disease.replace("___", " ")
        detected_disease = detected_disease.replace("_", " ")
        detected_disease = detected_disease.strip()

        print("Clean Disease:", detected_disease)

        # Exact match first
        disease_data = Disease.objects.filter(
            disease_name__iexact=detected_disease
        ).first()

        # fallback match
        if not disease_data:
            disease_data = Disease.objects.filter(
                disease_name__icontains=detected_disease
            ).first()

        print("DB Disease:", disease_data)

        # Medicines
        medicines = Medicine.objects.filter(
            disease__disease_name__icontains=detected_disease
        ).order_by('-effectiveness')

        # Products
        products = Product.objects.filter(
            disease__disease_name__icontains=detected_disease
        )

        # Save History
        DetectionHistory.objects.create(
            user=request.user,
            image=filename,
            disease=detected_disease
        )

    return render(request,'ai_engine/disease.html',{
        'disease': disease_data,
        'medicines': medicines,
        'products': products,
        'detected': detected_disease,
        'error': error
    })
# Yield Prediction View
def yield_prediction(request):

    result = None

    if request.method == "POST":

        soil = request.POST.get('soil')
        rainfall = request.POST.get('rainfall')
        temperature = request.POST.get('temperature')

        result = predict_yield(soil, rainfall, temperature)

    return render(request, 'ai_engine/yield.html', {'result': result})


# Soil Detection View
def soil_detection(request):

    result = None
    error = None

    if request.method == "POST":

        image = request.FILES.get('image')

        if not image:
            error = "Please upload image"
            return render(request,'ai_engine/soil.html',{
                'error': error
            })

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)

        image_path = fs.path(filename)

        result = detect_soil(image_path)

    return render(request, 'ai_engine/soil.html', {
        'result': result,
        'error': error
    })