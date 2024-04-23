from django import forms
from .models import UserInterest

class UserInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        fields = ['Job', 'Name', 'Email', 'Resume', 'Message']
        
