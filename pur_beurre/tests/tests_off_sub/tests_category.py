"""This module contains the tests related to the 'Category' class."""

from django.test import TestCase

from off_sub.models import Category, Product


class CategoryTestCase(TestCase):

    def setUp(self):
        # one category already recorded
        self.category_1 = Category.objects.create(name="desserts")
            
    def test_get_url_1k_products_right_category(self):
        """
        Test if the returned URL is well as expected.
        """
        url = "https://fr.openfoodfacts.org/cgi/search.pl?" \
                + "action=process&tagtype_0=categories" \
                + "&tag_contains_0=contains&tag_0=desserts" \
                + "&page_size=1000&json=1"
        self.assertEqual(self.category_1.get_url_1k_products(), url)

    def test_get_url_1k_products_wrong_category(self):
        """
        Test if the returned URL is an empty string.
        """
        category_0 = Category.objects.create(name="alcool")
        self.assertEqual(category_0.get_url_1k_products(), "")

    def test_add_category_to_db_one_new_record(self):
        """
        Test if one record has been added to the 'Category' table.
        """
        # count the number of categories
        old_categories_records = Category.objects.count()
        # add a new category
        category_2 = Category(name="poissons")
        category_2.add_category_to_db()
        # count the number of categories again
        new_categories_records = Category.objects.count()
        # compare the two numbers (after and before)
        self.assertEqual(new_categories_records, old_categories_records + 1)

    def test_add_category_to_db_already_exists(self):
        """
        Test if the 'Category' table stays unchanged
        if the category is already recorded.
        """
        # count the number of categories
        old_categories_records = Category.objects.count()
        # add a category already recorded
        category_1_bis = Category(name="desserts")
        category_1_bis.add_category_to_db()
        # count the number of categories again
        new_categories_records = Category.objects.count()
        # compare the two numbers (after and before)
        self.assertEqual(new_categories_records, old_categories_records)

    def test_get_categories_list(self):
        """
        Test if the categories list is well as expected.
        """
        result = [
            "desserts",
            "eaux",
            "fromages",
            "legumes",
            "pains",
            "pizzas",
            "poissons",
            "riz",
            "viandes",
        ]
        self.assertEqual(Category.get_categories_list(), result)