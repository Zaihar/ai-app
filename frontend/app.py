
import streamlit as st
import requests

st.title("AI CHATBOT")

text = st.text_input("Ask anything...")

if st.button("Ask AI"):
    if not text.strip():
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": text},
                timeout=60
            )

            if response.status_code == 200:
                try:
                    ans = response.json()
                    st.success(ans["response"])
                except (ValueError, KeyError):
                    st.error("Backend returned an invalid response.")
                    st.code(response.text)

            else:
                st.error(f"Backend error: {response.status_code}")
                st.code(response.text)

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to backend: {e}")