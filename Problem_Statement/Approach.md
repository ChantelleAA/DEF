So we create a database containing information about:
1. clients
2. cases
3. mediators
4. appointments

and any other tables needed which we am thinking about.
Then in order for the client to get the mediators matching his case, they fill in a form which we will create with django. since django is creates ORMs, it will take the form the client filled and save it in the database, and the mediators will also fill a form, for their availability and it goes into the database.

so when the client sends in the form and the database is updated, we have a code behind in python which finds all the mediators whose profile matches with some keywords in their case description, so the cases description will be preprocessed removing the unimportant words like articles, and tenses etc. then we use a transformer model to measure the level of similarity between the case description + case type and the mediator profile. the reason for the transformer is so that it does not necessarily look for word to word matching, but like the related words to a particular field.

You're welcome! Here's a step-by-step guide on what to do first to set up your system, starting from setting up your development environment to implementing the core functionalities.

### Step 1: Set Up Your Development Environment

1. **Install Python and Django**:
   - Install Python from [python.org](https://www.python.org/).
   - Install Django using pip:
     ```bash
     pip install django
     ```

2. **Set Up a New Django Project**:
   - Create a new Django project:
     ```bash
     django-admin startproject MediationSystem
     ```
   - Navigate to the project directory:
     ```bash
     cd MediationSystem
     ```
   - Create a new Django app:
     ```bash
     python manage.py startapp mediators
     ```

### Step 2: Define Your Models

1. **Update `models.py` in the mediators app**:

   ```python
   from django.db import models

   class Client(models.Model):
       CLAIM_TYPES = [
           ('appeals', 'Appeals'),
           ('aviation', 'Aviation'),
           ('business_dispute', 'Business Dispute'),
           ('chancery', 'Chancery'),
           ('clinical_negligence', 'Clinical Negligence'),
           ('construction', 'Construction'),
           ('costs', 'Costs'),
           ('employment', 'Employment'),
           ('family_children', 'Family – Children'),
           ('family_divorce', 'Family – Divorce'),
           ('family_financial', 'Family – Financial'),
           ('family_inheritance_act', 'Family – Inheritance Act'),
           ('fire_damage', 'Fire damage'),
           ('flood_damage', 'Flood damage'),
           ('personal_injury_abuse_claims', 'Personal Injury - Abuse claims'),
           ('personal_injury_cica', 'Personal Injury - CICA'),
           ('personal_injury_employer_liability', 'Personal Injury - Employer Liability'),
           ('personal_injury_mib_untraced', 'Personal Injury - MIB untraced'),
           ('personal_injury_military', 'Personal Injury - Military'),
           ('personal_injury_occupational_disease', 'Personal Injury - Occupational disease'),
           ('personal_injury_public_liability', 'Personal Injury - Public Liability (PL)'),
           ('personal_injury_road_traffic_whiplash', 'Personal injury - Road Traffic and Whiplash'),
           ('personal_injury_travel', 'Personal injury - Travel'),
           ('planning', 'Planning'),
           ('property_non_fire_flood', 'Property (non-fire/flood)'),
           ('shipping', 'Shipping'),
           ('travel_abta', 'Travel – ABTA'),
           ('travel_non_abta', 'Travel – non-ABTA'),
           ('workplace_issues', 'Workplace issues (not personal injury)')
       ]

       name = models.CharField(max_length=100)
       contact_info = models.TextField()
       claims = models.TextField()
       claim_type = models.CharField(max_length=50, choices=CLAIM_TYPES)

   class Mediator(models.Model):
       name = models.CharField(max_length=100)
       contact_info = models.TextField()
       expertise = models.JSONField()  # List of expertise areas
       experience = models.IntegerField()
       membership = models.TextField()
       style_approach = models.TextField()
       availability = models.JSONField()  # List of available days and times

   class Case(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       clients = models.ManyToManyField(Client)
       mediators = models.ManyToManyField(Mediator, through='Appointment')

   class Appointment(models.Model):
       case = models.ForeignKey(Case, on_delete=models.CASCADE)
       mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
       appointment_date = models.DateField()
       appointment_time = models.TimeField()
   ```

2. **Create and Apply Migrations**:
   - Create the migrations:
     ```bash
     python manage.py makemigrations mediators
     ```
   - Apply the migrations:
     ```bash
     python manage.py migrate
     ```

### Step 3: Create Forms for User Input

1. **Create Forms for Client and Mediator Input**:

   - **Forms for Client Input**:
     Create a form for clients to submit their details, claims, and claim types.

     ```python
     from django import forms
     from .models import Client

     class ClientForm(forms.ModelForm):
         class Meta:
             model = Client
             fields = ['name', 'contact_info', 'claims', 'claim_type']
     ```

   - **Forms for Mediator Input**:
     Create a form for mediators to submit their profiles.

     ```python
     from django import forms
     from .models import Mediator

     class MediatorForm(forms.ModelForm):
         class Meta:
             model = Mediator
             fields = ['name', 'contact_info', 'expertise', 'experience', 'membership', 'style_approach', 'availability']
     ```

   - **Forms for Case Input**:
     Create a form for cases to associate multiple clients.

     ```python
     from django import forms
     from .models import Case, Client

     class CaseForm(forms.ModelForm):
         clients = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple)

         class Meta:
             model = Case
             fields = ['title', 'description', 'clients']
     ```

### Step 4: Create Views to Handle Form Submission

1. **Views for Client, Mediator, and Case Input**:

   - **Views for Client Input**:
     Handle the submission of the client form.

     ```python
     from django.shortcuts import render, redirect
     from .forms import ClientForm

     def client_form_view(request):
         if request.method == 'POST':
             form = ClientForm(request.POST)
             if form.is_valid():
                 form.save()
                 return redirect('success')
         else:
             form = ClientForm()
         return render(request, 'client_form.html', {'form': form})
     ```

   - **Views for Mediator Input**:
     Handle the submission of the mediator form.

     ```python
     from django.shortcuts import render, redirect
     from .forms import MediatorForm

     def mediator_form_view(request):
         if request.method == 'POST':
             form = MediatorForm(request.POST)
             if form.is_valid():
                 form.save()
                 return redirect('success')
         else:
             form = MediatorForm()
         return render(request, 'mediator_form.html', {'form': form})
     ```

   - **Views for Case Input**:
     Handle the submission of the case form.

     ```python
     from django.shortcuts import render, redirect
     from .forms import CaseForm
     from .models import Case, Mediator

     def case_form_view(request):
         if request.method == 'POST':
             form = CaseForm(request.POST)
             if form.is_valid():
                 case = form.save()
                 return redirect('mediator_suggestions', case_id=case.id)
         else:
             form = CaseForm()
         return render(request, 'case_form.html', {'form': form})

     def mediator_suggestions_view(request, case_id):
         case = Case.objects.get(id=case_id)
         mediators = Mediator.objects.all()
         matched_mediators = match_mediators(case)
         return render(request, 'mediator_suggestions.html', {'case': case, 'mediators': matched_mediators})
     ```

### Step 5: Create the Matching Algorithm

1. **Enhanced Matching Algorithm**:

   ```python
   import nltk
   from nltk.corpus import wordnet
   from nltk.tokenize import word_tokenize

   def extract_keywords(claims):
       words = word_tokenize(claims)
       keywords = set(words)
       synonyms = set()

       for word in words:
           for syn in wordnet.synsets(word):
               for lemma in syn.lemmas():
                   synonyms.add(lemma.name())
       
       return keywords.union(synonyms)

   def match_mediators(case):
       keywords = set()
       claim_types = set()

       for client in case.clients.all():
           keywords.update(extract_keywords(client.claims))
           claim_types.add(client.claim_type)

       mediators = Mediator.objects.all()
       ranked_mediators = rank_mediators(keywords, claim_types, mediators)
       return ranked_mediators

   def rank_mediators(keywords, claim_types, mediators):
       ranked = []
       for mediator in mediators:
           match_score = sum(keyword in mediator.expertise for keyword in keywords)
           for claim_type in claim_types:
               if claim_type in mediator.expertise:
                   match_score += 5  # Arbitrary value to prioritize claim type match
           ranked.append((mediator, match_score))
       ranked.sort(key=lambda x: x[1], reverse=True)
       return [mediator for mediator, score in ranked]
   ```

### Step 6: Create Templates for User Interface

1. **Templates for Client, Mediator, and Case Forms**:

   - **Template for Client Form (`client_form.html`)**:

     ```html
     <form method="post">
         {% csrf_token %}
         {{ form.as_p }}
         <button type="submit">Submit</button>
     </form>
     ```

   - **Template for Mediator Form (`mediator_form.html`)**:

     ```html
     <form method="post">
         {% csrf_token %}
         {{ form.as_p }}
         <button type="submit">Submit</button>
     </form>
     ```

   - **Template for Case Form (`case_form.html`)
