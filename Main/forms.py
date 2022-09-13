from django import forms
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_content']
        widgets = {
            'note_title': forms.TextInput(attrs={
                'class': 'note_title',
                'placeholder': "Note Title"
            }),
            'note_content': forms.Textarea(attrs={
                'class': 'note_content',
                'placeholder': "Note Content",
            })
        }

class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_content']
        widgets = {
            'note_title': forms.TextInput(attrs={
                
            }),
            'note_content': forms.Textarea(attrs={
                'class': 'note_content',
                'placeholder': "Note Content",
            })
        }