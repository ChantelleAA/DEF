from django import forms
from .models import Mediator, Client, Case

class ClientCaseForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact_info', 'claims', 'claim_type']

    case_title = forms.CharField(max_length=200)
    case_description = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        client = super().save(commit=False)
        case_title = self.cleaned_data['case_title']
        case_description = self.cleaned_data['case_description']
        
        if commit:
            client.save()
            case = Case.objects.create(
                title=case_title,
                description=case_description
            )
            case.clients.add(client)
            case.save()
        return client

class MediatorForm(forms.ModelForm):
    class Meta:
        model = Mediator
        fields = ['name', 'contact_info', 'expertise', 'experience', 'membership', 'style_approach', 'availability']

