#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

class DogCatClassifier:
    def __init__(self, filename):
        self.filename = filename

    def preprocess_image(self):
        image_path = self.filename
        # Load the image
        img = load_img(image_path, target_size=(64, 64))
        # Convert the image to a numpy array
        img_array = img_to_array(img)
        # Expand dimensions to match the model's input format (adding batch size dimension)
        img_array = np.expand_dims(img_array, axis=0)
        # Normalize pixel values if your model expects normalization
        img_array /= 255.0
        print(img_array.shape)
        return img_array

    def prediction_dog_cat(self):
        # Load model
        model = load_model('model_new.h5')
        processed_image = self.preprocess_image()

        # Predict the class (0 for cat, 1 for dog)
        result = model.predict(processed_image)

        if result[0][0] > 0.5:
            prediction = 'dog'
        else:
            prediction = 'cat'
        return [{"image": prediction}]
    

# Example usage:
# image_path = 'cat.jpg'
# classifier = DogCatClassifier(image_path)
# prediction_result = classifier.prediction_dog_cat()
# print(prediction_result)