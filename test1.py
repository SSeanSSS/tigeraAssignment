import app
import unittest
import requests

class ApiTest(unittest.TestCase):
        RESULT_URL = "http://127.0.0.1:5000"

        #Test to check if the new webservice is returning correctly
        def test_1_get_result_url(self):
           # r = requests.get(ApiTest.RESULT_URL)
            r = requests.get(app.urijoke)
            self.assertEqual(r.status_code, 200)
            #self.assertEqual(len(str()), 0)

        # Test to check if the name webservice is returning correctly
        def test_2_get_NAME_url(self):
            r = requests.get(app.uriname)
            self.assertEqual(r.status_code, 200)

        # Test to check if the joke webservice is returning correctly
        def test_3_get_JOKE_url(self):
            r = requests.get(ApiTest.RESULT_URL)
            self.assertEqual(r.status_code, 200)
