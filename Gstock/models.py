from django.db import models
from django.utils.safestring import mark_safe


Nb_parts_choice = {
    ('0-3 ans', '0-3 ans'),
    ('4-14 ans', '4-14 ans'),
    ( '15-25 ans', '15-25 ans'),
    ('25-64 ans', '25-64 ans'),
    ('Plus de 65 ans', 'Plus de 65 ans'),
}
 
Mot_marie_choice = {
    ('Oui', 'Oui'),
    ('Non', 'Non'),
}


Carte_donnee_choice = {
    ('Oui', 'Oui'),
    ('Non', 'Non'),
}

Unite_choice = {
     ('Kilo', 'Kilo'),
    ('Unité', 'Unité'),
    ( 'Litre', 'Litre'),
}


class Beneficiaires(models.Model):
    Nom = models.CharField(max_length=200, blank=True, null=True)
    Prenom = models.CharField(max_length=200,blank=False, null=False)
    Email = models.EmailField(max_length=200, blank=True, null=True)
    Telephone = models.FloatField(max_length=20, blank=True, null=True)
    Nb_parts = models.CharField(choices = Nb_parts_choice, default = '1', max_length=200, blank=True, null=True)
    Mot_mairie = models.CharField(choices = Mot_marie_choice, default = '1', max_length=200, blank=False, null=False)
    Carte_donnee = models.CharField(choices = Carte_donnee_choice, default = '1', max_length=200, blank=False, null=False)
    Remarques = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.Nom


class Categories(models.Model):
    Nom = models.CharField(max_length=200, blank=False, null=False)
    Image = models.ImageField(upload_to='Gstock/Static/images', blank=True, null=True)
    Unite = models.CharField(choices = Unite_choice, default = '2', max_length=200)
    def __str__(self):
        return self.Nom

    @property
    def Logo(self):
        if self.Image:
            return mark_safe('<img src="{}" width="100" width="100" />' .format (self.Image.url))  # Get Image url
        return ""

 


class Stock(models.Model):
    Nom = models.CharField(max_length=200, blank=True, null=True)
    Categorie = models.ForeignKey(Categories,  on_delete=models.CASCADE, blank = True, null = True)
    Quantite = models.FloatField(default= '0', blank=True, null=True )
    Seuil_alerte  = models.IntegerField(default='0', blank=True, null=True)
    def __str__(self):
        return self.Nom

