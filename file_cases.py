from file_test import sum1
from unittest import TestCase

class SumTestCase(TestCase):
    def setUp(self):
        print("hello")
        self.file_obj = open("testfile.txt")
    
    def test_sum1_positive(self):
        self.assertEqual(sum1(file_obj=self.file_obj), 60)
    
    def test_sum1_negative(self):
        self.assertNotEqual(sum1(file_obj=self.file_obj), 50)
    
    def tearDown(self):
        print("tear")
        self.file_obj.close()
        return super().tearDown()