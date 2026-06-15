import streamlit as st
import google.genai as genai

# ----------------------------
# API KEY (Streamlit Secrets)
# ----------------------------
api_key = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

st.title("🌍 AI Translator")

text = st.text_area("Enter text in any language")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
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