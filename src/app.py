import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
    st.image(
        image,
        caption=f"You amazing image has shape {image.shape[:2]}",
        use_column_width=True,
    )

else:
    demo_image = "images/demo.jpg"
    image = np.array(Image.open(demo_image))
    st.image(
        image, caption=f"This is the demo image", use_column_width=True,
    )

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
st.write(f"blob.shape : {blob.shape}")
