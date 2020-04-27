"""
This module contains the unit tests related to
the db_update custom command (app 'off_sub').
"""

import os
import codecs
from unittest.mock import patch, Mock

from django.test import TestCase
from django.core.management import call_command
from requests import Response

from off_sub.models import Product, Category, Store
from tests.unit_tests_off_sub.tests_db_init import (
    MockCategory, MockRequestsGet as InitMockRequestsGet
)


class UpdateMockRequestsGet:

    CSV_MOCK_FILE = """
    code	product_name	nutriscore_grade	nutriscore_score	"""
    """url	image_url	fat_value	fat_unit	saturated-fat_value	"""
    """saturated-fat_unit	sugars_value	sugars_unit	salt_value	"""
    """salt_unit	another_key\n"1234567890123"	"a nice product"	"""
    """"b"	1	"a_nice_url"	"a_nice_image_url"	"""
    """10	"g"	10	"g"	10	"g"	10	"mg"	"another_value"\n
    """

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
    @patch(target='off_sub.models.Category', new=MockCategory)
    @patch(target='requests.get', new=InitMockRequestsGet)
    # @patch(target='requests.get', new=UpdateMockRequestsGet)
    def setUpClass(cls):
        super().setUpClass()
        # initialize the database
        call_command('db_init')
        # # update the database
        # call_command('db_update')
        # get a product
        # cls.prod_a = Product.objects.all()[0]

    @patch(target='requests.get', new=UpdateMockRequestsGet)
    def setUp(self):
        # update the database
        call_command('db_update')
        self.prod_a = Product.objects.all()[0]        

    def test_update_product_name(self):
        """
        Test if product name is updated.
        """
        self.assertEqual(self.prod_a.product_name, "a nice product")

    # def test_update_nutriscore_grade(self):
    #     """
    #     Test if product nutriscore grade is correct.
    #     """
    #     self.assertEqual(self.prod_a.nutriscore_grade, "b")

    # def test_update_nutriscore_score(self):
    #     """
    #     Test if product nutriscore score is updated.
    #     """
    #     self.assertEqual(self.prod_a.nutriscore_score, 1)

    # def test_update_url(self):
    #     """
    #     Test if product url is updated.
    #     """
    #     self.assertEqual(self.prod_a.url, "a_nice_url")

    # def test_update_image_url(self):
    #     """
    #     Test if product image url is updated.
    #     """
    #     self.assertEqual(self.prod_a.image_url, "a_nice_image_url")

    # def test_update_fat(self):
    #     """
    #     Test if fat data are updated.
    #     """
    #     self.assertEqual(self.prod_a.fat, "10g")

    # def test_update_saturated_fat(self):
    #     """
    #     Test if saturated fat data are updated.
    #     """
    #     self.assertEqual(self.prod_a.saturated_fat, "10g")

    # def test_update_sugars(self):
    #     """
    #     Test if sugars data are updated.
    #     """
    #     self.assertEqual(self.prod_a.sugars, "10g")

    # def test_update_salt(self):
    #     """
    #     Test if salt data are updated.
    #     """
    #     self.assertEqual(self.prod_a.salt, "10mg")
