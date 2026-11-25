from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ton nom'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ton adresse email'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Sujet du message'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Écris ton message ici...',
                'rows': 5
            }),
        }
