from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class LoginForm(forms.Form):
    id = forms.CharField(label='id', max_length = 100) 
    password = forms.CharField(label='password', max_length = 20)


class NewElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        exclude = ['admin', 'region_id', 'winner', 'election_id']
    def __init__ (self, *args, **kwargs):
        super(NewElectionForm, self).__init__(*args, **kwargs)
        self.fields["candidates"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["date_created"].widget = forms.widgets.DateInput(
            attrs={'placeholder': 'dd-mm-yy', 'type': 'text',
                   'onfocus': "(this.type='date')"}
        )
        self.fields["start_time"].widget = forms.widgets.TimeInput(
            attrs={'placeholder': 'hr:min', 'type': 'text', 'onfocus': "(this.type='time')"}
        )
        self.fields["end_time"].widget = forms.widgets.TimeInput(
            attrs={'placeholder': 'hr:min', 'type': 'text', 'onfocus': "(this.type='time')"}
        )
        self.fields["candidates"].queryset = Candidate.objects.all()
        # region = Region.objects.get(region_name='Thane')
        # self.fields["candidates"].queryset = region.candidate_set.all()
        # self.fields["candidates"].queryset = Election.objects.filter(admin=admin)

class VoterForm(ModelForm):
    class Meta:
        model = Voter
        exclude = ['admin','voter_id', 'age', 'vote', 'election']
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(VoterForm, self).__init__(*args, **kwargs)
        self.fields["date_of_birth"].widget = forms.widgets.DateInput(
            attrs={'placeholder': 'dd-mm-yy', 'type': 'text',
                   'onfocus': "(this.type='date')"}
        )

class AddCandidateForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['candidate_id', 'region']