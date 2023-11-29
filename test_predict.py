import unittest

from predict import get_prediction
from utils import get_bytes_from_image

class TestDenseNetModel(unittest.TestCase):
    def test_cat_image_inference(self):

        image_path = './test_images/cat_image.jpeg'
        img_bytes = get_bytes_from_image(image_path)

        prediction = get_prediction(img_bytes)

        self.assertEqual(prediction, ['n02124075', 'Egyptian_cat'])