
from django.shortcuts import render, redirect
from .models import *
from .Forms import *
from .models import Beneficiaires as Beneficiaires1
from .models import Stock as Stock1
from .models import Categories as Categories1
from django.http import HttpResponse
import csv
from django.contrib import messages


def Stock(request):
    title = "Stock"
    header = "Stock"
    form = StockSearchForm(request.POST or None)
    queryset = Stock1.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset,
        "header" : header,
        "form" : form,
    } 

    if request.method == 'POST':
        queryset = Stock1.objects.filter(Nom__icontains=form['Nom'].value(
        )
        )
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] ='attachment ; filename = "Stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['Nom', 'Categorie', 'Quantite', 'Seuil_alerte'])
            instance = queryset
            for obj in instance :
                writer.writerow([obj.Nom, obj.Categorie, obj.Quantite, obj.Seuil_alerte])
            return response
        context = {
        "form" : form,
        "header" : header,
        "queryset" : queryset,
    }
    
    return render(request, "Stock.html",context)


def Ajout_Produit(request):
    header = "Ajout"
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/Ajout_Produit')
    context = {
        "form" : form,
        "title" : "Ajout",
        "header" : header,
    }
    return render(request, "Ajout_Produit.html", context)
        

def update_Stock(request, pk):
    queryset = Stock1.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/Stock')
    context = {
        'form' : form
    }
    return render(request, 'Ajout_Produit.html',context)

def delete_produit(request, pk):
    queryset = Stock1.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Saved')
        return redirect('/Stock')
    return render(request, 'delete_produit.html')


def Seuil_alerte(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = SeuilalerteForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/Stock")
    context = {
            "instance": queryset,
            "form": form,
            }
    return render(request, "Ajout_Produit.html", context)



def Beneficiaires(request):
    title = "Beneficiaires"
    header = "Beneficiaires"
    form = BeneficiairesSearchForm(request.POST or None)
    queryset = Beneficiaires1.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset,
        "header" : header,
        "form" : form,
    }
    if request.method == 'POST':
        queryset = Beneficiaires1.objects.filter(Nom__icontains=form['Nom'].value(
        ), Nb_parts__icontains=form['Nb_parts'].value()
        )
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] ='attachment ; filename = "Beneficiaires.csv"'
            writer = csv.writer(response)
            writer.writerow(['Nom', 'Prenom', 'Email', 'Telephone', 'Nb_parts', 'Mot_mairie', 'Carte_donnee', 'Remarques'])
            instance = queryset
            for obj in instance :
                writer.writerow([obj.Nom, obj.Prenom, obj.Email, obj.Telephone, obj.Nb_parts, obj.Mot_mairie, obj.Carte_donnee, obj.Remarques])
            return response
        context = {
        "form" : form,
        "header" : header,
        "queryset" : queryset,
    }
    
    return render(request, "Beneficiaires.html",context)



def Ajout_Beneficiaires(request):
    header = "Ajout"
    form = BeneficiairesForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/Ajout_Beneficiaires')
    context = {
        "form" : form,
        "title" : "Ajout",
        "header" : header,
    }
    return render(request, "Ajout_Beneficiaires.html", context)


def update_Beneficiaires(request, pk):
    queryset = Beneficiaires1.objects.get(id=pk)
    form = BeneficiairesUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = BeneficiairesUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/Beneficiaires')
    context = {
        'form' : form
    }
    return render(request, 'Ajout_Beneficiaires.html',context)


def delete_beneficiaires(request, pk):
    queryset = Beneficiaires1.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Saved')
        return redirect('/Beneficiaires')
    return render(request, 'delete_beneficiaires.html')

