"""
Test classes for /msa/progressive route
"""
import unittest
import json

from app import APP

APP.testing = True

VAID_DATA_FILE_NAME = 'test/API/MSA_Progressive/valid_data.json'
INVAID_DATA_FILE_NAME = 'test/API/MSA_Progressive/invalid_data.json'

# python -m coverage run -m unittest discover


class MSAProgressiveRouteTestValid(unittest.TestCase):
    """
    Test class to test /msa/progressive route with valid data
    """

    def setUp(self):
        self.client = APP.test_client()
        with open(VAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        """
        method to test the response code is 200
        """
        for item in self.data:
            result = self.client.post(
                '/msa/progressive', data=json.dumps(item),
                headers={'Content-Type': 'application/json'})
            # print(result.status)
            self.assertEqual(result.status, '200 OK',
                             'failed input:\n'+str(item)+'\n'+str(result.data))


class MSAProgressiveRouteTestInvalid(unittest.TestCase):
    """
    Test class to test /msa/progressive route with invalid data
    """

    def setUp(self):
        self.client = APP.test_client()
        with open(INVAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        """
        method to test the response code is 400
        """
        for item in self.data:
            result = self.client.post(
                '/msa/progressive', data=json.dumps(item),
                headers={'Content-Type': 'application/json'})
            # print(result.data)
            self.assertEqual(result.status, '400 BAD REQUEST',
                             'failed input:\n'+str(item)+'\n'+str(result.data))
