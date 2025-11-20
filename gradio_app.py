import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

model_path = 'plant_disease_model_finetuned.keras'  
model = load_model(model_path)

classes = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight']

def predict_disease(image):
    # 1. Preprocess the image to match training inputs
    # Resize to 224x224
    image = tf.image.resize(image, (224, 224))
    # Expand dims to (1, 224, 224, 3)
    img_array = tf.expand_dims(image, 0)
    
    # 2. Predict
    predictions = model.predict(img_array)
    scores = tf.nn.softmax(predictions[0])
    
    # 3. Create a dictionary of labels and probabilities
    results = {}
    for i, class_name in enumerate(classes):
        results[class_name] = float(scores[i])
    
    return results

# Create the Interface
interface = gr.Interface(
    fn=predict_disease,
    inputs=gr.Image(type="numpy", label="Upload Plant Leaf"),
    outputs=gr.Label(num_top_classes=3, label="Disease Prediction"),
    title="Syngenta Plant Disease Doctor",
    description="Upload a photo of a Corn, Apple, Cherry, or Blueberry leaf to detect diseases."
)

# Launch
interface.launch(share=True)