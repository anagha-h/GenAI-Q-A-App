from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input, image):
    if input != "":
        response=model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    
    return response.text

st.set_page_config(page_title="Q&A Page")

st.header("Gemini Image App")

input=st.text_input("Input Prompt: ", key="input")

upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit=st.button("Tell me about the image")

if submit:
    response=get_gemini_response(input, image)
    st.subheader("The answer is: ")
    st.write(response)