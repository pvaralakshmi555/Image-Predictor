import tensorflow 
from tensorflow import keras
import cv2
import numpy as np
import argparse

vgg16 = keras.applications.VGG16() # pretrained model for performing image classification (1000 classes)
parse=argparse.ArgumentParser()
parse.add_argument("--imagepath",type=str,required=True,help="pass the image path")
args=parse.parse_args()
path=args.imagepath
image =keras.utils.load_img(path,target_size=(224,224,3))
input_args=keras.utils.img_to_array(image)
input_arr=np.array([input_args])
prediction=vgg16.predict(input_arr)
print(np.argmax(prediction))