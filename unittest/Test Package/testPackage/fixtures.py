
from testDevelopmentCode.multiModule import pow2num,add2num

import unittest


def setUpModule():
    print('Executed before an test in the module')

def tearDownModule():
    print('Executed after all tests in module are run')


class Testadd2num(unittest.TestCase):
    def setUp(self):
        print('Executed before start of every test')

    def tearDown(self):
        print('Executed at the end of every test')

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)
	  
    def test_sum_3pos_num(self):
      self.assertEqual(add2num(20,40), 60) 
	  
	  
class Testpow2num(unittest.TestCase):

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)
        
    @classmethod
    def setUpClass(cls):
        print('Executed before any test in the class runs.')

    @classmethod
    def tearDownClass(cls):
        print('Executed after all tests in class are run.')

    

		

if __name__=='__main__':
    unittest.main()	  