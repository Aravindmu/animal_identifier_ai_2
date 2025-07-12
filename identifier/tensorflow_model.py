import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights='imagenet')##which model we are using to predict the animal name. Here we are using MobileNetV2 with ImageNet weights.

def predict_animal(img_path):
    img = image.load_img(img_path, target_size=(224, 224))## Loading the image and resizing it to 224x224 pixels, which is the input size for MobileNetV2.use "image" is handle image loading and processing before passing it to a deep learning model.
    img_array = image.img_to_array(img) ## output is a numpy array of shape (224, 224, 3) representing the image.
    img_array = np.expand_dims(img_array, axis=0)##output is a numpy array of shape (1, 224, 224, 3), which is the expected input shape for the model.
    img_array = preprocess_input(img_array)## Preprocessing the image array to match the input requirements of MobileNetV2 or validation for satisfing the model's input requirements. This step typically includes scaling pixel values and normalizing the image data.
    predictions = model.predict(img_array)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0] ##top=1 ensures only the highest-confidence prediction is returned.decode_predictions(predictions, top=1)[0] extracts the first (and only) prediction.
    return decoded_preds[0][1]  # Returns predicted animal name ,(class_ID, predicted_label, confidence_score) ,[('n02124075', 'Egyptian_cat', 0.95)]
##decoded_preds[0] accesses the first tuple: ('n02124075', 'Egyptian_cat', 0.95).

##decoded_preds[0][1] extracts the second item: 'Egyptian_cat' (the predicted name).

