import unittest
from acme import Product
<<<<<<< HEAD
from acme_report import generate_products,ADJECTIVES,NOUNS
from random import randint


class AcmeProductTests(unittest.TestCase):
=======
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.testCase):
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
    def test__price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 5)
        
        
    def test__weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        
    def test_stealability_and_exploductivity(self):
        prod = Product('BOMB', weight=7, flammability=100)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!!')
        
class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        inventory = generate_products()
        self.assertEqual(len(inventory), 30)
        
    def test_legal_names(self):
        inventory = generate_products()
        names = [x.name for x in inventory]
        for n in names:
            self.assertEqual(len(n.split(' ')), 2)
            
<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ = __main__:
>>>>>>> a03f3728f3dae925a75a37a9b60278234a43d116
    unittest.main()