import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from PIL import Image
import joblib

dataset_path = "dataset/PlantVillage"

images = []
labels = []

# Load dataset
for folder in os.listdir(dataset_path):

    folder_path = os.path.join(dataset_path, folder)

    if not os.path.isdir(folder_path):
        continue

    for img in os.listdir(folder_path):

        img_path = os.path.join(folder_path, img)

        try:
            # Open image
            image = Image.open(img_path)

            # Convert to RGB (important)
            image = image.convert('RGB')

            # Resize to same size
            image = image.resize((64, 64))

            # Convert to numpy array
            image = np.array(image)

            # Ensure shape is correct
            if image.shape == (64, 64, 3):
                images.append(image.flatten())
                labels.append(folder)

        except Exception as e:
            print("Error:", img_path)


# Convert to numpy
X = np.array(images)
y = np.array(labels)

print("Total images loaded:", len(X))


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
print("Training model...")

model = RandomForestClassifier(
    n_estimators=30,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Training completed")

# Test model
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))


# Save model
joblib.dump(model, "plant_model.pkl")

print("Model trained successfully")