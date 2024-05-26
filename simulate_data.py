import pandas as pd
import random
from faker import Faker
import datetime

fake = Faker()

# Define constants and helper functions
CLAIM_TYPES = [
    'appeals', 'aviation', 'business_dispute', 'chancery', 'clinical_negligence', 'construction', 'costs', 'employment', 
    'family_children', 'family_divorce', 'family_financial', 'family_inheritance', 'fire_damage', 'flood_damage', 
    'personal_injury_abuse_claims', 'personal_injury_cica', 'personal_injury_employer_liability', 'personal_injury_mib_untraced', 
    'personal_injury_military', 'personal_injury_occupational_disease', 'personal_injury_public_liability', 
    'personal_injury_road_traffic_whiplash', 'personal_injury_travel', 'planning', 'property_non_fire_flood', 
    'shipping', 'travel_abta', 'travel_non_abta', 'workplace_issues'
]

def generate_fake_clients(num_entries):
    clients = []
    for i in range(num_entries):
        clients.append({
            "id": i + 1,
            "name": fake.name(),
            "contact_info": f"{fake.email()}, {fake.phone_number()}",
            "claims": f"Claim {i*2+1}, Claim {i*2+2}",
            "claim_type": random.choice(CLAIM_TYPES),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(clients)

def generate_fake_mediators(num_entries):
    mediators = []
    for i in range(num_entries):
        mediators.append({
            "id": i + 1,
            "name": fake.name(),
            "contact_info": f"{fake.email()}, {fake.phone_number()}",
            "expertise": str([fake.word() for _ in range(2)]),
            "experience": random.randint(1, 30),
            "membership": fake.word(),
            "style_approach": fake.sentence(),
            "availability": str([fake.day_of_week() for _ in range(2)]),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(mediators)

def generate_fake_cases(num_entries):
    cases = []
    for i in range(num_entries):
        cases.append({
            "id": i + 1,
            "title": f"Case {i + 1}",
            "description": fake.text(),
            "case_type": random.choice(CLAIM_TYPES),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(cases)

def generate_fake_case_clients(num_entries, num_cases, num_clients):
    case_clients = []
    for i in range(num_entries):
        case_clients.append({
            "id": i + 1,
            "case_id": random.randint(1, num_cases),
            "client_id": random.randint(1, num_clients),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(case_clients)

def generate_fake_appointments(num_entries, num_cases, num_mediators):
    appointments = []
    for i in range(num_entries):
        appointments.append({
            "id": i + 1,
            "case_id": random.randint(1, num_cases),
            "mediator_id": random.randint(1, num_mediators),
            "appointment_date": fake.date_this_year().isoformat(),
            "appointment_time": fake.time(),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(appointments)

def generate_fake_keywords(num_entries):
    keywords = []
    for i in range(num_entries):
        keywords.append({
            "id": i + 1,
            "word": fake.word(),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(keywords)

def generate_fake_case_keywords(num_entries, num_cases, num_keywords):
    case_keywords = []
    for i in range(num_entries):
        case_keywords.append({
            "id": i + 1,
            "case_id": random.randint(1, num_cases),
            "keyword_id": random.randint(1, num_keywords),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(case_keywords)

def generate_fake_mediator_keywords(num_entries, num_mediators, num_keywords):
    mediator_keywords = []
    for i in range(num_entries):
        mediator_keywords.append({
            "id": i + 1,
            "mediator_id": random.randint(1, num_mediators),
            "keyword_id": random.randint(1, num_keywords),
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        })
    return pd.DataFrame(mediator_keywords)

# Generate the data
num_entries = 50

clients = generate_fake_clients(num_entries)
mediators = generate_fake_mediators(num_entries)
cases = generate_fake_cases(num_entries)
case_clients = generate_fake_case_clients(num_entries, num_entries, num_entries)
appointments = generate_fake_appointments(num_entries, num_entries, num_entries)
keywords = generate_fake_keywords(num_entries)
case_keywords = generate_fake_case_keywords(num_entries, num_entries, num_entries)
mediator_keywords = generate_fake_mediator_keywords(num_entries, num_entries, num_entries)

# Save to CSV
clients.to_csv('/mnt/data/clients.csv', index=False)
mediators.to_csv('/mnt/data/mediators.csv', index=False)
cases.to_csv('/mnt/data/cases.csv', index=False)
case_clients.to_csv('/mnt/data/case_clients.csv', index=False)
appointments.to_csv('/mnt/data/appointments.csv', index=False)
keywords.to_csv('/mnt/data/keywords.csv', index=False)
case_keywords.to_csv('/mnt/data/case_keywords.csv', index=False)
mediator_keywords.to_csv('/mnt/data/mediator_keywords.csv', index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Clients", dataframe=clients)


