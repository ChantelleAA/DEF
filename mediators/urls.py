# mediators/urls.py

from django.urls import path
from .views import client_case_form_view, mediator_suggestions_view

urlpatterns = [
    path('client_case/', client_case_form_view, name='client_case_form'),
    path('mediators/<int:case_id>/', mediator_suggestions_view, name='mediator_suggestions'),
]
