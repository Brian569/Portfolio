from .models import *
from django import forms

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('name', 'icon', 'background', 'about_image', 'about_text')
