import streamlit as st
import random

st.title("🎲 Találd ki a számot!")

# Csak egyszer generáljon számot
if "szam" not in st.session_state:
    st.session_state.szam = random.randint(1, 100)

tipp = st.number_input(
    "Adj meg egy számot 1 és 100 között:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Tippelés"):
    if tipp < st.session_state.szam:
        st.warning("📉 Túl kicsi!")
    elif tipp > st.session_state.szam:
        st.warning("📈 Túl nagy!")
    else:
        st.success("🎉 Gratulálok! Eltaláltad!")
