import random

# Dummy Soil Detection Model

def detect_soil(image):

    soil_types = [
        "Clay Soil",
        "Loamy Soil",
        "Sandy Soil",
        "Black Soil"
    ]

    return random.choice(soil_types)