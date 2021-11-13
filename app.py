import streamlit as st
from PIL import Image

st.title("Webcam image input demo app!!")

image_file = st.camera_image_input()

if image_file is not None:
    x = st.slider("ROTATE TO X DEGREE", 0, 360, 0)

    pil_image = Image.open(image_file)
    rotated_iamge = pil_image.rotate(x)
    st.image(rotated_iamge)
