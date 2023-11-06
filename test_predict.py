import unittest

from predict import get_prediction
from utils import get_bytes_from_image, download_image

class TestDenseNetModel(unittest.TestCase):
    def test_cat_image_inference(self):
        
        image_url = 'https://i.imgur.com/t5S6rkz.jpg'

        download_image(image_url, '/tmp/image.jpg')
        img_bytes = get_bytes_from_image('/tmp/image.jpg')

        prediction = get_prediction(img_bytes)

        self.assertEqual(prediction, ['n02124075', 'Egyptian_cat'])