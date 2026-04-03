import hashlib
from products.models import Disease

def predict_plant_disease(image_path):

    # Get diseases from database
    diseases = list(
        Disease.objects.values_list('disease_name', flat=True)
    )

    # If no disease in DB
    if not diseases:
        return "No Disease Found"

    # Create stable hash
    hash_value = hashlib.md5(image_path.encode()).hexdigest()

    index = int(hash_value, 16) % len(diseases)

    return diseases[index]