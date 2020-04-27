"""
This module contains the unit tests related to
the db_update custom command (app 'off_sub').
"""

import os
from unittest.mock import patch

from django.test import TestCase
from django.core.management import call_command

from off_sub.models import Product


class UpdateMockRequestsGet:

    def __init__(self, url=None, stream=True, params=None):
        self.status_code = 200

    def __enter__(self):
        self.file = open(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'csv_db',
            'test.csv'
        ), 'rU')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False

    def iter_lines(self):
        self.file.seek(0)
        for line in self.file.readlines():
            yield bytes(line, 'utf8')

    def raise_for_status(self):
        pass


class DatabaseUpdateTestCase(TestCase):

    @classmethod
    @patch(target='requests.get', new=UpdateMockRequestsGet)
    def setUpClass(cls):
        super().setUpClass()
        # create a product
        cls.prod = Product.objects.create(
            code='1234567890123',
            product_name="a superb product",
            nutriscore_grade='a',
            nutriscore_score=-20,  # fictive (not calculated)
            url="a_superb_url",
            image_url="a_superb_image_url",
            fat="0g",
            saturated_fat="0g",
            sugars="0g",
            salt="0mg"
        )
        # update the database
        call_command('db_update')
        # get the (updated) product
        cls.prod = Product.objects.all()[0]

    def test_update_product_name(self):
        """
        Test if product name is updated.
        """
        self.assertEqual(self.prod.product_name, "a nice product")

    def test_update_nutriscore_grade(self):
        """
        Test if product nutriscore grade is correct.
        """
        self.assertEqual(self.prod.nutriscore_grade, "b")

    def test_update_nutriscore_score(self):
        """
        Test if product nutriscore score is updated.
        """
        self.assertEqual(self.prod.nutriscore_score, 1)

    def test_update_url(self):
        """
        Test if product url is updated.
        """
        self.assertEqual(self.prod.url, "a_nice_url")

    def test_update_image_url(self):
        """
        Test if product image url is updated.
        """
        self.assertEqual(self.prod.image_url, "a_nice_image_url")

    def test_update_fat(self):
        """
        Test if fat data are updated.
        """
        self.assertEqual(self.prod.fat, "10g")

    def test_update_saturated_fat(self):
        """
        Test if saturated fat data are updated.
        """
        self.assertEqual(self.prod.saturated_fat, "10g")

    def test_update_sugars(self):
        """
        Test if sugars data are updated.
        """
        self.assertEqual(self.prod.sugars, "10g")

    def test_update_salt(self):
        """
        Test if salt data are updated.
        """
        self.assertEqual(self.prod.salt, "10mg")
