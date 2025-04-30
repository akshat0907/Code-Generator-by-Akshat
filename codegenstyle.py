import os
import google.generativeai as genai
import streamlit as st

# st.set_page_config(page_title="Code Generator", layout="wide")
st.title('Code Generator by Akshat')

os.environ['GOOGLE_API_KEY'] = "AIzaSyBl31kKtxz3e4mIpm9oTqfRi3gcth3I-1g"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

st.markdown("""
<style>
    .stTextArea {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton:hover {
        background-color: #45a049;
    }
    .stSelectbox {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

user_input = st.text_area("Enter Problem Statement", height=150)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001")

option = st.selectbox(
    'Select Programming Language',
    ('Python', 'C', 'C++', 'JAVA')
)

if st.button('Generate'):
    prompt = f"""
    You are an expert coder, who is good at coding a given problem statement into target programming language.
    Help me code the problem statement into: {option}.
    
    ```
    {user_input}
    ```
    """
    response = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001").generate_content(prompt)
    st.success(response.text)

st.markdown("""
<style>
    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)