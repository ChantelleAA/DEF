# Case to Mediators Matching and Scheduling System

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Algorithm](#algorithm)
6. [Data Models](#data-models)


## Introduction

The Mediation Matching and Scheduling System is designed to efficiently connect clients with mediators based on their availability, expertise, and other relevant criteria. The system ensures that both parties can meet at mutually convenient times while also aligning the mediator's skills with the client's specific needs.

## Project Structure

```
MediationSystem/
├── MediationSystem/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── mediators/
│   │   ├── __pycache__/
│   │   ├── management/
│   │   │   ├── __pycache__/
│   │   │   ├── commands/
│   │   │       ├── __init__.py
│   │   ├── migrations/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   ├── templates/
│   │       ├── appointment_success.html
│   │       ├── availability_success.html
│   │       ├── book_appointment.html
│   │       ├── booking_success.html
│   │       ├── client_case_form.html
│   │       ├── client_success.html
│   │       ├── home.html
│   │       ├── mediator_availability.html
│   │       ├── mediator_profile_display.html
│   │       ├── mediator_profile_form.html
│   │       ├── mediator_profile.html
│   │       ├── mediator_success.html
│   │       ├── mediator_suggestions.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
├── db.sqlite3
├── manage.py
└── populate_mediators.py
```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/mediation-matching-scheduling.git
   cd mediation-matching-scheduling
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Usage

1. **Run the Application:**
   ```bash
   python manage.py runserver
   ```

2. **Open a Browser and Navigate to:**
   ```
   http://127.0.0.1:8000/
   ```

## Algorithm

### Matching and Scheduling Algorithm

The matching and scheduling algorithm ensures that the mediator selected for a case meets the client's criteria and that all parties can meet at a mutually convenient time.

#### Key Features

1. **Client-Mediator Matching**:
   - **Availability**: Matches clients with mediators based on overlapping available times.
   - **Expertise**: Ensures mediators have the appropriate level of expertise and language proficiency required by the client.

2. **Scheduling**:
   - **Availability Management**: Allows both clients and mediators to input their available times and days.


