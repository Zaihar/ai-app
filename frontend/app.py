import streamlit as st 
import requests

st.title("AI CHATBOT")

text = st.text_input("ask anyrhing... ")

if st.button("ask ai "):
    response = requests.post(
    'http://127.0.0.1:8000/chat',
    json={"question":text}
    )

    ans = response.json()
    st.success(ans["response"])