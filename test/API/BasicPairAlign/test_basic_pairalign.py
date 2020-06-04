"""
Test classes for /pair/nw route
"""
import unittest
import json

from app import APP

APP.testing = True

VAID_DATA_FILE_NAME = 'test/API/BasicPairAlign/valid_data.json'
INVAID_DATA_FILE_NAME = 'test/API/BasicPairAlign/invalid_data.json'

# python -m coverage run -m unittest discover


class NWRouteTestValid(unittest.TestCase):

    def setUp(self):
        self.client = APP.test_client()
        with open(VAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        for item in self.data:
            result = self.client.post(
                '/pair/nw', data=json.dumps(item), headers={'Content-Type': 'application/json'})
            # print(result.status)
            self.assertEqual(result.status, '200 OK','failed input:\n'+str(item))


class NWRouteTestInvalid(unittest.TestCase):

    def setUp(self):
        self.client = APP.test_client()
        with open(INVAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        for item in self.data:
            result = self.client.post(
                '/pair/nw', data=json.dumps(item), headers={'Content-Type': 'application/json'})
            # print(result.data)
            self.assertEqual(result.status, '400 BAD REQUEST', 'failed input:\n'+str(item))


class SWRouteTestValid(unittest.TestCase):

    def setUp(self):
        self.client = APP.test_client()
        with open(VAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        for item in self.data:
            result = self.client.post(
                '/pair/sw', data=json.dumps(item), headers={'Content-Type': 'application/json'})
            # print(result.status)
            self.assertEqual(result.status, '200 OK', 'failed input:\n'+str(item))


class SWRouteTestInvalid(unittest.TestCase):

    def setUp(self):
        self.client = APP.test_client()
        with open(INVAID_DATA_FILE_NAME, 'r') as file:
            self.data = json.load(file)

    def tearDown(self):
        del self.client

    def test_route(self):
        for item in self.data:
            result = self.client.post(
                '/pair/sw', data=json.dumps(item), headers={'Content-Type': 'application/json'})
            # print(result.data)
            self.assertEqual(result.status, '400 BAD REQUEST', 'failed input:\n'+str(item))
            