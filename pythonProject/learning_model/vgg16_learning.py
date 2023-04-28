import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Dense, Flatten
from keras.applications.vgg16 import VGG16

import cv2

DATASET_PATH = 'C:/Users/LunaticWorld/Desktop/Workspace/junsup/2023'
FOOD_CLASSES = ['carrot', 'chilli_pepper', 'garlic', 'onion', 'potato', 'raddish']
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

def resize_image(img):
    img_resized = cv2.resize(img, IMG_SIZE)
    return img_resized

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    preprocessing_function=resize_image  # 이미지 resize 함수를 preprocessing_function 인자로 추가
)

train_generator = train_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, 'train'),
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

x = vgg16.output
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(len(FOOD_CLASSES), activation='softmax')(x)

model = Model(inputs=vgg16.input, outputs=predictions)

for layer in vgg16.layers:
    layer.trainable = False

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

EPOCHS = 10
STEP_SIZE_TRAIN = train_generator.n // train_generator.batch_size

model.fit(train_generator, epochs=EPOCHS, steps_per_epoch=STEP_SIZE_TRAIN)

test_datagen = ImageDataGenerator(
    rescale=1./255,
    preprocessing_function=resize_image  # 이미지 resize 함수를 preprocessing_function 인자로 추가
)

test_generator = test_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, 'test'),
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

STEP_SIZE_TEST = test_generator.n // test_generator.batch_size

scores = model.evaluate(test_generator, steps=STEP_SIZE_TEST)
print(f'Test loss: {scores[0]}')
print(f'Test accuracy: {scores[1]}')

model.save('test_6labels.h5')