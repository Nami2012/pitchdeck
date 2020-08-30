from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    Name = forms.CharField(max_length= 30,required = False,help_text='Optional')
    email = forms.EmailField(max_length = 254,help_text='Required.Inform a valid email address')
    class Meta:
        model = User
        fields = ('username','Name','email','password1','password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class pitchDeckForm(forms.ModelForm):
    class Meta:
        model = pitchDeck
        fields = ['startupName']

class titleSlideForm(forms.ModelForm):
    class Meta:
        model = titleSlide
        fields = ['name','titleline']

class problemTryingToSolveForm(forms.ModelForm):
    class Meta:
        model = problemTryingToSolve
        fields = ['bullet1','bullet2','bullet3','bullet4','bullet5']


class visionForm(forms.ModelForm):
    class Meta:
        model = vision
        fields = ['bullet1','bullet2','bullet3','bullet4','bullet5']


class uniqueValuePropositionForm(forms.ModelForm):
    class Meta:
        model = uniqueValueProposition
        fields = ['usp','bullet1','bullet2','bullet3','bullet4','bullet5']


class milestonesForm(forms.ModelForm):
    class Meta:
        model = milestones
        fields = ['impact1','bullet1','impact2','bullet2','bullet3','bullet4','bullet5']

class totalAddressableMarketForm(forms.ModelForm):
    class Meta:
        model = totalAddressableMarket
        fields = ['totalAvailableMarket','servedAvailableMarket','targetMarket','TAMSection','SAMSection','TMSection']

class businessModalForm(forms.ModelForm):
    class Meta:
        model = businessModal
        fields = ['customerAcquisitionStrategy','serviceProvision','modelType','monetizationStrategy']
        
class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['startupsFree','startupsPaid','incumbentsFree','incumbentsPaid']

class competitiveAdvantageForm(forms.ModelForm):
    class Meta:
        model = competitiveAdvantage
        fields = ['impact1','bullet1']

