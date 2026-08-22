import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Az én chatbotom")

if "uzenetek" not in st.session_state:
    st.session_state.uzenetek = []
    
# korábbi üzenetek kirajzolása
for uz in st.session_state.uzenetek:
    with st.chat_message(uz["role"]):
        st.write(uz["text"])

kerdes = st.chat_input("Kérdezz valamit!")

if kerdes:
    st.session_state.uzenetek.append({"role": "user", "text": kerdes})
    with st.chat_message("user"):
        st.write(kerdes)

    def valaszol():
        for chunk in client.models.generate_content_stream(
                model="gemini-3.6-flash", contents=kerdes):
            yield chunk.text

    
    with st.chat_message("assistant"):
        teljes =st.write_stream(valaszol())
    st.session_state.uzenetek.append({"role": "assistant", "text": teljes})
