from app import app

import unittest

class TestPredictionsAPI(unittest.TestCase):
    def test_cat_image_response(self):
        self.app = app
        self.client = self.app.test_client

        request = {
            'image_url': 'https://i.imgur.com/t5S6rkz.jpg'
        }

        response = self.client().post('/predict', data=request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['class_id'], 'n02124075')

    def test_invalid_image_response(self):
        self.app = app
        self.client = self.app.test_client

        request = {
            'image_url': 'https://i.imgur.com/THIS_IS_A_BAD_URL.jpg'
        }

        response = self.client().post('/predict', data=request)
        self.assertEqual(response.status_code, 500)
