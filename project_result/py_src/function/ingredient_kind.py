import os

import cv2
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

def get_kind(img_url):
    np.set_printoptions(suppress=True)
    # Load the model
    model = load_model("../model/keras_model.h5", compile=False)
    # model = load_model("model/base_vgg16.h5", compile=False)

    # Load the labels
    class_names = open("../model/labels.txt", "r", encoding="utf-8").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(img_url).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    # image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image = image.resize((224, 224), resample=Image.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name[2:].replace('\n', '')