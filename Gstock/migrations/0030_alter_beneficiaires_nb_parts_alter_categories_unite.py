# Generated by Django 4.2.11 on 2024-04-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gstock', '0029_alter_beneficiaires_carte_donnee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaires',
            name='Nb_parts',
            field=models.CharField(blank=True, choices=[('0-3 ans', '0-3 ans'), ('Plus de 65 ans', 'Plus de 65 ans'), ('15-25 ans', '15-25 ans'), ('25-64 ans', '25-64 ans'), ('4-14 ans', '4-14 ans')], default='1', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='Unite',
            field=models.CharField(choices=[('Kilo', 'Kilo'), ('Unité', 'Unité'), ('Litre', 'Litre')], default='2', max_length=200),
        ),
    ]
