import unittest
import json
from add import add1

class AddTestCase(unittest.TestCase):
    def setUp(self) :
        f = open("sample_data.json", 'r')
        data = json.load(f)
        self.positive_actual = data["test_positive"]["actual_value"]
        self.positive_val1 = data["test_positive"]["val1"]
        self.positive_val2 = data["test_positive"]["val2"]
        self.negative_actual = data["test_negative"]["actual_value"]
        self.negative_val1 = data["test_negative"]["val1"]
        self.negative_val2 = data["test_negative"]["val2"]

    def test_add1_positive(self):
        actual_value = self.positive_actual
        expected_value = add1(self.positive_val1,self.positive_val2)
        self.assertEqual(actual_value, expected_value)
    
    def test_add1_negative(self):
        actual_value = self.negative_actual
        expected_value = add1(self.negative_val1,self.negative_val2)
        self.assertNotEqual(actual_value, expected_value)

if __name__ == "__main__":
    unittest.main()