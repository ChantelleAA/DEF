from django.shortcuts import render, redirect
from .forms import ClientCaseForm, MediatorForm
from .models import Case, Mediator

#  USE SUCCESS AFTER FORM IS FILLED
# # def client_case_form_view(request):
# #     if request.method == 'POST':
# #         form = ClientCaseForm(request.POST)
# #         if form.is_valid():
# #             form.save()

# #             return redirect('success')  # Redirect to the success URL pattern
# #     else:
# #         form = ClientCaseForm()
# #     return render(request, 'client_case_form.html', {'form': form})


# VIEW SCRIPT WITH MEDIATOR PROFILES SHOWING AT OUTPUT
def client_case_form_view(request):
    if request.method == 'POST':
        form = ClientCaseForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            case_title = form.cleaned_data['case_title']
            case_description = form.cleaned_data['case_description']
            client.save()
            case = Case.objects.create(
                title=case_title,
                description=case_description
            )
            case.clients.add(client)
            case.save()
            return redirect('mediator_suggestions', case_id=case.id)
    else:
        form = ClientCaseForm()
    return render(request, 'client_case_form.html', {'form': form})

def mediator_suggestions_view(request, case_id):
    case = Case.objects.get(id=case_id)
    mediators = Mediator.objects.all()
    matched_mediators = match_mediators(case)
    return render(request, 'mediator_suggestions.html', {'case': case, 'mediators': matched_mediators})

def home_view(request):
    return redirect('client_case_form')  # Redirect to the client case form

def success_view(request):
    return render(request, 'success.html')  # Render a simple success page

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def match_mediators(case):
    claim_types = set()

    for client in case.clients.all():
        claim_types.add(client.claim_type)

    mediators = Mediator.objects.all()
    ranked_mediators = rank_mediators(claim_types, mediators)
    return ranked_mediators

def rank_mediators(claim_types, mediators):
    ranked = []
    for mediator in mediators:
        match_score = 0
        for expertise in mediator.expertise:
            for claim_type in claim_types:
                if claim_type.lower() in expertise.lower():
                    match_score += 100  # Arbitrary high value for an exact match
                elif any(word in claim_type.lower() for word in expertise.lower().split()):
                    match_score += 50  # Lower value for a partial match
        ranked.append((mediator, match_score))
    
    # Sort mediators by match score in descending order
    ranked.sort(key=lambda x: x[1], reverse=True)
    
    # Filter mediators with match_score > 100 and limit to top 10
    filtered_ranked = [mediator for mediator, score in ranked if score > 100][:10]
    
    return filtered_ranked

#  SELECT MEDIATOR BASED ON MATCHING KEYWORDS
# # def extract_keywords(claims):
# #     words = word_tokenize(claims)
# #     keywords = set(words)
# #     synonyms = set()

# #     for word in words:
# #         for syn in wordnet.synsets(word):
# #             for lemma in syn.lemmas():
# #                 synonyms.add(lemma.name())
    
# #     return keywords.union(synonyms)

# # def match_mediators(case):
# #     keywords = set()
# #     claim_types = set()

# #     for client in case.clients.all():
# #         keywords.update(extract_keywords(client.claims))
# #         claim_types.add(client.claim_type)

# #     mediators = Mediator.objects.all()
# #     ranked_mediators = rank_mediators(keywords, claim_types, mediators)
# #     return ranked_mediators

# # def rank_mediators(keywords, claim_types, mediators):
# #     ranked = []
# #     for mediator in mediators:
# #         match_score = sum(keyword in mediator.expertise for keyword in keywords)
# #         for claim_type in claim_types:
# #             if claim_type in mediator.expertise:
# #                 match_score += 50  # Arbitrary value to prioritize claim type match
# #         ranked.append((mediator, match_score))
# #     ranked.sort(key=lambda x: x[1], reverse=True)
# #     return [mediator for mediator, score in ranked]

