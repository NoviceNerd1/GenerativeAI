##
## AI Iamge to text Generator : Using Gemini-pro-vision
##


from dotenv import load_dotenv
load_dotenv() ## load all the environment var

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input!="":
        response= model.generate_content([input, image])
    elif(image== FileNotFoundError):
        response= model.generate_content(input)
    else:
        response= model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image AI")


st.header("Gemini Application")

input= st.text_input("Input : ",key="input")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png","webp"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit= st.button("Tell me about the image: ")

if(submit):
    response= get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)