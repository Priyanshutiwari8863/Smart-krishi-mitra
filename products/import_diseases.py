import csv
from products.models import Disease

with open('diseases.csv', newline='') as file:

    reader = csv.DictReader(file)

    for row in reader:
        Disease.objects.create(
            plant=row['plant'],
            disease_name=row['disease_name'],
            symptoms=row['symptoms'],
            solution=row['solution']
        )

print("Diseases imported successfully")