import cricdata
import unittest 
import mock 

class Myclass():
    def __init__(self, data):
        self.data = data 
    def json(self):
        return self.data

class CricTestCase(unittest.TestCase):
    @mock.patch("cricdata.make_get_call")
    def  test_India_series(self, get_data):
        get_data.return_value = {"data": [{"name": "India is"}]}
        res = cricdata.get_India_series()
        self.assertTrue(res)
    
    @mock.patch("cricdata.requests.get")
    def  test_India_series(self, get_data):
        get_data.return_value = Myclass({"data": [{"name": "India is"}]})
        res = cricdata.get_India_series()
        self.assertTrue(res)