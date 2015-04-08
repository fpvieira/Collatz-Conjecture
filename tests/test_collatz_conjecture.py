#-*- coding:utf-8 -*- 
import unittest
from src.collatz_conjecture import decompose_number, execute

class TestCollatzConjecture(unittest.TestCase):

    def test_decompose_number_with_even_number(self):
        self.assertEquals(2, decompose_number(2))

    def test_decompose_number_with_odd_number(self):
        self.assertEquals(8, decompose_number(3))        
    
if __name__ == "__main__":
    unittest.main()