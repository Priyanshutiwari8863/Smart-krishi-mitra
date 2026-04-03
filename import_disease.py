import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishi_project.settings')
django.setup()

from products.models import Disease

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(BASE_DIR, "diseases.csv")

with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:

        plant = row['plant'].strip()
        disease_name = row['disease_name'].strip()
        symptoms = row['symptoms'].strip()
        solution = row['solution'].strip()

        # Avoid duplicate entries
        Disease.objects.get_or_create(
            plant=plant,
            disease_name=disease_name,
            defaults={
                'symptoms': symptoms,
                'solution': solution
            }
        )

print("✅ Data Imported Successfully")