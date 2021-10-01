from sample_module import add2num
from multiModule import pow2num

import unittest

class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)
	  
    def test_sum_3pos_num(self):
      self.assertEqual(add2num(20,40), 60) 
	  
	  
class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)
		

if __name__=='__main__':
    unittest.main()	  
	 