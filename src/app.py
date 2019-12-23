import streamlit as st
import cv2
from PIL import Image
import numpy as np

img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
image = np.array(Image.open(img_file_buffer))

if image is not None:
    st.image(
        image,
        caption=f"You amazing image has shape {image.shape[:2]}",
        use_column_width=True,
    )
