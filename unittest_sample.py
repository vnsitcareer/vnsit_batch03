import unittest
from add import add1

class AddTestCase(unittest.TestCase):
    def test_add1_positive(self):
        actual_value = 10
        expected_value = add1(6,4)
        self.assertEqual(actual_value, expected_value)
    
    def test_add1_negative(self):
        actual_value = 12
        expected_value = add1(6,4)
        self.assertEqual(actual_value, expected_value)

if __name__ == "__main__":
    unittest.main()