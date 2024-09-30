from django import forms
from .models import Carte

class CarteForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = ['nom', 'postnom', 'prenom', 'email', 'sexe', 'telephone', 'date_naissance', 'lieu_naissance', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "Nom"}),
            'postnom': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "Post-nom"}),
            'prenom': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Prénom'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Prénom'}),
            'sexe': forms.Select(attrs={'class': 'form-control mb-3'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Téléphone'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Date de naissance. Format: JJ/MM/AA'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lieu de naissance'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Adresse'}),
        }
        