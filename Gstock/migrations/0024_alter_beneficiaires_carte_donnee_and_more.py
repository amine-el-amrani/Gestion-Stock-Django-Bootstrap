# Generated by Django 4.2.11 on 2024-04-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gstock', '0023_alter_beneficiaires_carte_donnee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaires',
            name='Carte_donnee',
            field=models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='beneficiaires',
            name='Mot_mairie',
            field=models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='beneficiaires',
            name='Nb_parts',
            field=models.CharField(blank=True, choices=[('Plus de 65 ans', 'Plus de 65 ans'), ('0-3 ans', '0-3 ans'), ('4-14 ans', '4-14 ans'), ('15-25 ans', '15-25 ans'), ('25-64 ans', '25-64 ans')], default='1', max_length=200, null=True),
        ),
    ]
