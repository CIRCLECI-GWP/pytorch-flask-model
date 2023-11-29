from app import app

import unittest

# From CircleCI's CIRCLECI-GWP/pytorch-flask-model's repository
cat_image_url = "https://raw.githubusercontent.com/CIRCLECI-GWP/pytorch-flask-model/06d0d0ea0d05dd9792e93a9db63678797c018d4a/test_images/cat_image.jpeg"

class TestPredictionsAPI(unittest.TestCase):
    def test_cat_image_response(self):
        self.app = app
        self.client = self.app.test_client

        request = {
            'image_url': cat_image_url
        }

        response = self.client().post('/predict', data=request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['class_id'], 'n02124075')

    def test_invalid_image_response(self):
        self.app = app
        self.client = self.app.test_client

        request = {
            'image_url': 'https://github.com/CIRCLECI-GWP/THIS_IS_A_BAD_URL.jpg'
        }

        response = self.client().post('/predict', data=request)
        self.assertEqual(response.status_code, 500)
