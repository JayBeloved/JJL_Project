# jjltech/apps/pitchdeck/forms.py
from django import forms
from .models import PitchDeck

class PitchDeckForm(forms.ModelForm):
    class Meta:
        model = PitchDeck
        fields = ('pitch', 'industry', 'instagram', 'linkedin', 'website', 'twitter', 'facebook', 'youtube')
        # widgets = {
        #     'pitch': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Pitch'}),
        #     'industry': forms.Select(attrs={'placeholder': 'Industry'}),
        #     'instagram': forms.TextInput(attrs={'placeholder': 'Instagram URL'}),
        #     'linkedin': forms.TextInput(attrs={'placeholder': 'LinkedIn URL'}),
        #     'website': forms.URLInput(attrs={'placeholder': 'Website URL'}),
        #     'twitter': forms.TextInput(attrs={'placeholder': 'Twitter URL'}),
        #     'facebook': forms.TextInput(attrs={'placeholder': 'Facebook URL'}),
        #     'youtube': forms.TextInput(attrs={'placeholder': 'YouTube URL'}),
        # }