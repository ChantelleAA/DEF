import pandas as pd
import os
import json
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediationSystem.settings')
django.setup()

from mediators.models import Mediator

# Path to your .xlsx file
file_path = 'mediator_profiles.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

def to_json_array(value):
    if isinstance(value, str):
        return json.dumps(value.split(','))
    return json.dumps(value)

# Iterate over DataFrame rows
for index, row in df.iterrows():
    # Create a new Mediator object
    mediator = Mediator(
        name=row['name'],
        contact_info=row['contact_info'],
        expertise=to_json_array(row['expertise']),  # Convert to JSON array
        experience=row['experience'],
        membership=row['membership'],
        style_approach=row['style_approach'],
        availability=to_json_array(row['availability'])  # Convert to JSON array
    )
    # Save the mediator object to the database
    mediator.save()

print("Database populated successfully!")
