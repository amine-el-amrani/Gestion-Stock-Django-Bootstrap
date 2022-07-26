from django.contrib import admin
from django.urls import path
from Gstock import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Stock', views.Stock, name = 'Stock' ),
    path('Beneficiaires', views.Beneficiaires, name = 'Beneficiaires' ),
    path('admin/', admin.site.urls),
    path('Ajout_Produit', views.Ajout_Produit, name = 'Ajout_Produit' ),
    path('Ajout_Beneficiaires', views.Ajout_Beneficiaires, name = 'Ajout_Beneficiaires' ),
    path('update_Stock/<str:pk>/', views.update_Stock, name = 'update_Stock' ),
    path('update_Beneficiaires/<str:pk>/', views.update_Beneficiaires, name = 'update_Beneficiaires' ),
    path('delete_produit/<str:pk>/', views.delete_produit, name = 'delete_produit' ),
    path('delete_beneficiaires/<str:pk>/', views.delete_beneficiaires, name = 'delete_beneficiaires' ),
    path('Seuil_alerte/<str:pk>/', views.Seuil_alerte, name="Seuil_alerte"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
