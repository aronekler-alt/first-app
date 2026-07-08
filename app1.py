
import streamlit as st

st.title("csapatod pontjai")

sajatgol = st.number_input("mennyi gólt rugott a csapatod?", min_value=1, step=1)
ellenfelgol = st.number_input("mennyi gólt rugott az ellenfél csapata?", min_value=1, step=1)


pont = 0

if sajatgol > ellenfelgol:
    pont = 3
elif sajatgol < ellenfelgol:  
    pont = 0
elif sajatgol == ellenfelgol:  
    pont = 1

st.write(f"Pont: {pont}")