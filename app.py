import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = load_model("my_model.h5")

# Compile the model (optional if saved with optimizer/loss, but safe)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Define class names
class_names = ['plastic', 'organic', 'metal']

# Get model input shape
input_shape = model.input_shape 
st.write(f"Model expects input of shape: {input_shape}")

# Streamlit UI
st.title("Image Classification App")
st.write("Upload an image and the model will predict its category.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption='Uploaded Image', width=200)

    target_size = (input_shape[1], input_shape[2])
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Predicted class: **{predicted_class}**")
