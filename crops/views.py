import requests
from django.shortcuts import render
 #api_key = "579b464db66ec23bdd0000013cb55814fb6d4acd682fc996249cddb7Y"




import requests
from django.shortcuts import render

def market(request):

    api_key = "579b464db66ec23bdd0000013cb55814fb6d4acd682fc996249cddb7Y"



    state = request.GET.get("state")

    url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={api_key}&format=json&limit=2000"

    try:
        response = requests.get(url)
        data = response.json()
        records = data.get("records", [])
    except:
        records = []

    # Default value
    state_records = records

    # Filter state
    if state:
        state_records = [
            r for r in records
            if state.lower() in r.get("state","").lower()
        ]

    # Vegetable list
    vegetables = [
        "Tomato","Onion","Potato","Brinjal",
        "Cauliflower","Cabbage","Carrot",
        "Green Chilli","Bhindi","Radish",
        "Peas","Beans"
    ]

    # Filter vegetables
    veg_records = [
        r for r in state_records
        if any(v.lower() in r.get("commodity","").lower() for v in vegetables)
    ]

    # fallback
    final_records = veg_records if veg_records else state_records

    return render(request,'crops/market.html',{
        "data":final_records,
        "state":state
    })
def crop_list(request):

    crops = [
        {"name":"Rice","soil":"Clay, Loamy","season":"Kharif","water":"Low"},
        {"name":"Wheat","soil":"Loamy, Clay","season":"Rabi","water":"Low"},
        {"name":"Maize","soil":"Loamy, Clay","season":"Rabi, Kharif","water":"Low"},
        {"name":"Mustard","soil":"Loamy","season":"Rabi","water":"Low"},
        {"name":"Bajra","soil":"Sandy","season":"Kharif","water":"Low"},
        {"name":"Tomato","soil":"Sandy Loam","season":"All Season","water":"Low"},
        {"name":"Potato","soil":"Sandy Loam","season":"Rabi","water":"Low"},
        {"name":"Sugarcane","soil":"Loamy","season":"All Season","water":"High"},
        {"name":"Cotton","soil":"Black Soil","season":"Kharif","water":"Medium"},
    ]

    return render(request,"crops/crop_list.html",{
        "crops":crops
    })