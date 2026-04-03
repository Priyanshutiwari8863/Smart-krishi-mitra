import pickle
import numpy as np

model = pickle.load(open('plant_model.pkl', 'rb'))

def predict_disease(image):
    prediction = model.predict(image)
    return prediction[0]