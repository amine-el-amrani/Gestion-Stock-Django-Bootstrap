from django.contrib import admin
from .models import *
from .Forms import *
from import_export.admin import ImportExportModelAdmin



class AdminForm1(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['Nom', 'Prenom', 'Email', 'Telephone', 'Nb_parts', 'Mot_mairie', 'Carte_donnee', 'Remarques']
    form = BeneficiairesForm
    list_filter = ['Nom']
    search_fields = ['Nom']



class AdminForm2(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Logo','Nom','Unite']
    form = CategoriesForm
    list_filter = ['Nom']
    readonly_fields = ['Logo']
    search_fields = ['Nom']


    def Logo(self, obj):
        return obj.Logo

    Logo.short_description = 'Logo'
    Logo.allow_tags = True



class AdminForm3(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Nom', 'Categorie', 'Quantite', 'Seuil_alerte']
    form = StockForm
    list_filter = ['Nom', 'Categorie']
    search_fields = ['Nom', 'foreinkeyfield__Categorie']


admin.site.site_header = 'Gestion de Stock'
admin.site.register(Beneficiaires, AdminForm1)
admin.site.register(Categories, AdminForm2)
admin.site.register(Stock, AdminForm3)
