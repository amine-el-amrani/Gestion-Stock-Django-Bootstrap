from django import forms
from .models import *





class BeneficiairesForm(forms.ModelForm):
    class Meta:
        model = Beneficiaires
        fields = ['Nom', 'Prenom', 'Email', 'Telephone', 'Nb_parts', 'Mot_mairie', 'Carte_donnee', 'Remarques']


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['Nom', 'Image', 'Unite']



class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Nom', 'Categorie', 'Quantite', 'Seuil_alerte']



class StockSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields =  ['Nom']
        

class SeuilalerteForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Seuil_alerte']



class StockUpdateForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields = ['Nom', 'Categorie', 'Quantite', 'Seuil_alerte']


class BeneficiairesSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Beneficiaires
        fields =  ['Nom', 'Nb_parts']

class BeneficiairesUpdateForm(forms.ModelForm):
    class Meta :
        model = Beneficiaires
        fields = ['Nom', 'Prenom', 'Email', 'Telephone', 'Nb_parts', 'Mot_mairie', 'Carte_donnee', 'Remarques']


