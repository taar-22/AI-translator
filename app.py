import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
st.title("🌍 AI Translator")

text = st.text_area("Enter text in any language")

if st.button("Translate"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Translate the following text into English.
        Only return the English translation.

        {text}
        """
    )

    st.subheader("English Translation")
    st.write(response.text)