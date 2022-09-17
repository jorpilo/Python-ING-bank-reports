import unittest
from cgi import test

from pythoningreport.categories import Category, match_categories


class TestCategoryClass(unittest.TestCase):
    def test_match_exact_singleterm(self):
        test_category = Category("test", "test description", ["test"])
        self.assertTrue(test_category.match("test"))
        
    def test_match_exact_casesensitive(self):
        test_category = Category("test", "test description", ["test"])
        self.assertTrue(test_category.match("TEST"))
        
    def test_match_exact_multipleterms(self):
        test_category = Category("test", "test description", ["test", "other"])
        self.assertTrue(test_category.match("test"))
        self.assertTrue(test_category.match("other"))
        
    def test_match_nonexact(self):
        test_category = Category("test", "test description", ["test", "othertest"])
        self.assertTrue(test_category.match("testfirst"))
        
    def test_match_middle(self):
        test_category = Category("test", "test description", ["test", "twotest"])
        self.assertTrue(test_category.match("somethingtestotherthing"))
        
    def test_nomatch(self):
        test_category = Category("test", "test description", ["test", "test2"])
        self.assertFalse(test_category.match("other"))

class TestMultipleCategories(unittest.TestCase):
    
    def test_single_exact_match(self):
        self.assertEqual(match_categories("Daiso"), "Shopping")

    def test_single_non_exact(self):
        test_category = Category("Transport", "Transport", ["UBER", "CARSHAREAUS","OPAL", "TRANSPORT"])
        self.assertEqual(match_categories("OPALCARD", categories=[test_category]), "Transport")
        self.assertEqual(match_categories("CARDOPALCARD", categories=[test_category]), "Transport")
        self.assertEqual(match_categories("OPALCARD"), "Transport")
        self.assertEqual(match_categories("CARDOPALCARD"), "Transport")
