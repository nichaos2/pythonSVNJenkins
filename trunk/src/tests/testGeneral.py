'''
Created on 18 avr. 2019

@author: nioannou
'''
import unittest

from main import sum, concatanate
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
        result = sum(data)
        self.assertEqual(result, 1)


    def test_bad_type(self):
        '''
        This test pass a type that will make the function throw an error
        You can define a different type of error
        However, this is because we have definde the total=0
        '''
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
            
    def test_concatanate(self):
        '''
        This test 
        '''
        data = ["banana","tyropita"]
        result = concatanate(data)
        self.assertEqual(result, 'bananatyropita')
        
        
    def setUp(self):
        self.app = 'my data'
        
    def test_smth(self):
        print(self.app)
        
        
if __name__ == '__main__':
    unittest.main()