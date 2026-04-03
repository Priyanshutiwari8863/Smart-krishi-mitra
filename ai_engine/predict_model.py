import joblib
import numpy as np
from PIL import Image

# Load trained model
model = joblib.load("plant_model.pkl")


def predict_plant_disease(image_path):

    # Open image
    image = Image.open(image_path)

    # Convert RGB
    image = image.convert('RGB')

    # Resize
    image = image.resize((64,64))

    # Convert to numpy
    image = np.array(image).flatten().reshape(1, -1)

    # Predict
    prediction = model.predict(image)

    return prediction[0]