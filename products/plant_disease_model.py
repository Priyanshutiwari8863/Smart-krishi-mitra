import random

def predict_plant_disease(image):

    diseases = [
        "Early Blight",
        "Late Blight",
        "Leaf Mold",
        "Powdery Mildew",
        "Bacterial Spot",
        "Healthy"
    ]

    return random.choice(diseases)