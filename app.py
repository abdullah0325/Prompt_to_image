
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Retrieve API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image(prompt: str, model: str = "dall-e-3", size: str = "1024x1024", quality: str = "standard"):
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )
    return response.data[0].url

# Streamlit UI
st.title("Generate Image using DALL-E3")
user_prompt = st.text_input("Enter prompt for image generation")

if st.button("Generate Image"):
    combined_prompt = user_prompt + " write the name  'ABDULLAH' in small size on top write corner of imge in lovely style"
    with st.spinner("Generating image..."):
        image_url = generate_image(combined_prompt)
        st.image(image_url)
