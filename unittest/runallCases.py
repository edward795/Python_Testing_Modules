from sample_module import add2num

import unittest

class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)
	  
    def test_sum_3pos_num(self):
      self.assertEqual(add2num(20,40), 60) 

if __name__=='__main__':
    unittest.main()	  
	 