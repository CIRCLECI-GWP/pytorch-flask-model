from flask import Flask, jsonify, request

from utils import download_image, get_bytes_from_image
from predict import get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Image Classification API!'

if __name__ == '__main__':
    app.run()

tmp_dir = '/tmp'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        imageUrl = request.form['image_url']
        try:
            filename = download_image(imageUrl, tmp_dir + '/image.jpg')

            img_bytes = get_bytes_from_image(filename)

            class_id, class_name = get_prediction(image_bytes=img_bytes)
            return jsonify({'class_id': class_id, 'class_name': class_name})
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500