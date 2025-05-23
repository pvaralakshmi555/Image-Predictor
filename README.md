# Image-Predictor

This project uses a pretrained VGG16 model from Keras to perform image classification on 1000 ImageNet categories.

## Features

- Uses Keras' VGG16 pretrained model
- Accepts image path as input argument
- Predicts the most likely class
- Outputs ImageNet class index

### Install from requirements.txt

pip install -r requirements.txt

## Run the Aplication 
  Use the following command to run the image prediction app with your image path:

python app.py --imagepath "path/to/your/image.jpg"
