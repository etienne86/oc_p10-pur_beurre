"""
This command is automatically executed on a weekly basis, with 'manage.py',
to update the database 'pur_beurre_db'.
Pre-requisite: the command 'db_init' has to be executed initially.
"""

import csv
import codecs
import datetime

import requests
import django
from django.shortcuts import get_object_or_404
from django.core.management.base import BaseCommand

from off_sub.models import Product


class Command(BaseCommand):
    help = 'Update the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(
            f"{datetime.datetime.now().isoformat(' ', 'seconds')} [info] "
            "Mise à jour de la base de données, veuillez patienter SVP..."
        ))
        url = "https://static.openfoodfacts.org/data/" \
            "fr.openfoodfacts.org.products.csv"
        counter = 0
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            reader = csv.DictReader(
                codecs.iterdecode(response.iter_lines(), 'utf-8'),
                delimiter='\t'
            )
            for record in reader:
                product_code = record["code"]
                try:
                    product = get_object_or_404(Product, code=product_code)
                    product.update_fields(record)
                    counter += 1
                except django.http.response.Http404:
                    pass
        self.stdout.write(self.style.SUCCESS(
            f"{datetime.datetime.now().isoformat(' ', 'seconds')} [info] "
            f"Tâche terminée : {counter} produit(s) mis à jour !"
        ))
