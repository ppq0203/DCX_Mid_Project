import os

import cv2
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

from PIL import Image  # Install pillow instead of PIL
import numpy as np

# model = load_model("model/converted_keras3/keras_model.h5")
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# DATASET_PATH = 'img'
# FOOD_CLASSES = ['감자', '계란','고추', '당근','대파','마늘', '무', '배추', '양파']
# IMG_SIZE = (224, 224)
# BATCH_SIZE = 16
#
# def resize_image(img):
#     img_resized = cv2.resize(img, IMG_SIZE)
#     return img_resized
#
# test_datagen = ImageDataGenerator(
#     rescale=1./255,
#     preprocessing_function=resize_image
# )
#
# test_generator = test_datagen.flow_from_directory(
#     os.path.join(DATASET_PATH, 'test'),
#     target_size=IMG_SIZE,
#     batch_size=BATCH_SIZE,
#     class_mode='categorical'
# )
#
# STEP_SIZE_TEST = test_generator.n // test_generator.batch_size
#
# scores = model.evaluate(test_generator, steps=STEP_SIZE_TEST)
# print(f'Test loss: {scores[0]}')
# print(f'Test accuracy: {scores[1]}')
#
# STEP_SIZE_TEST = test_generator.n // test_generator.batch_size
#
# model = load_model("best_model_base_vgg16.h5", compile=False)
#
# # Load the labels
# class_names = open("model/converted_keras/labels.txt", "r", encoding="utf-8").readlines()
#
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#
# scores = model.evaluate(test_generator, steps=STEP_SIZE_TEST)
# print(f'Test loss: {scores[0]}')
# print(f'Test accuracy: {scores[1]}')

# #############################################
# Disable scientific notation for clarity

# np.set_printoptions(suppress=True)
#
# # Load the model
# model = load_model("model/converted_keras3/keras_model.h5", compile=False)
# # model = load_model("model/base_vgg16.h5", compile=False)
#
# # Load the labels
# class_names = open("model/converted_keras/labels.txt", "r", encoding="utf-8").readlines()
#
# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#
# # Replace this with the path to your image
# image = Image.open("test_img/po2.jpg").convert("RGB")
#
# # resizing the image to be at least 224x224 and then cropping from the center
# size = (224, 224)
# # image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
# image = image.resize((224, 224), resample=Image.LANCZOS)
#
# # turn the image into a numpy array
# image_array = np.asarray(image)
#
# # Normalize the image
# normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)
