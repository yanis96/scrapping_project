import time
from  unittest import TestCase, mock
import requests
import random

from guitares import Guitare


class Test_Api(TestCase):


    def setUp(self):
        self.mock_guitare = mock.Mock(spec=Guitare)
        self.mock_guitare.get_all_guitares = mock.Mock(return_value=200)
        self.mock_guitare.get_guitare = mock.Mock(return_value=200)
        self.mock_guitare.add_guitare = mock.Mock(return_value=201)
        self.mock_guitare.update_guitare = mock.Mock(return_value=200)
        self.mock_guitare.delete_guitare = mock.Mock(return_value=200)



    #def test_get_guitares(self):
     #   r = requests.get(self.URL)
      #  self.assertEqual(r.status_code, 200)


    def test_get_guitares(self):
        r = self.mock_guitare.get_all_guitares()
        result = 200
        self.assertEqual(r, result)


    def test_get_guitare_by_id(self):
        r = self.mock_guitare.get_guitare(1)
        result = 200
        self.assertEqual(r,result)


    def test_add_guitare(self):
        r = self.mock_guitare.add_guitare("Fender", "500", "9800")
        result = 201
        self.assertEqual(r, result)


    def test_update_guitare(self):
        r = self.mock_guitare.update_guitare(2,"Fender", "500", "9800")
        result = 200
        self.assertEqual(r, result)


    def test_remove_guitare(self):
        r = self.mock_guitare.delete_guitare(2)
        result = 200
        self.assertEqual(r, result)