"""
This command is automatically executed on a weekly basis, with 'manage.py',
to update the database 'pur_beurre_db'.
Pre-requisite: the command 'db_init' has to be executed initially.
"""

import csv
import os
import codecs

import requests
import django
from django.shortcuts import get_object_or_404
from django.core.management.base import BaseCommand

from off_sub.models import Category, Product, Store


class Command(BaseCommand):
    help = 'Update the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(
            "Mise à jour de la base de données, veuillez patienter SVP..."
        ))
        # télécharger le fichier CSV depuis OFF ?
        url = "https://static.openfoodfacts.org/data/" \
            "fr.openfoodfacts.org.products.csv"
        # attendre que le fichier soit complètement chargé
        # lire le fichier csv de la bdd off
        counter = 0
        
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            reader = csv.DictReader(
                codecs.iterdecode(response.iter_lines(), 'utf-8'),
                delimiter='\t'
            )
            for record in reader:
                print("record : ", record)
                print("FOR")
                product_code = record["code"]
                try:
                    print("TRY")
                    product = get_object_or_404(Product, code=product_code)
                    product.update_fields(record)
                    counter += 1
                except django.http.response.Http404:
                    pass
        self.stdout.write(self.style.SUCCESS(
            f"Tâche terminée : {counter} produit(s) mis à jour !"))