import streamlit as st

st.title("Az első weboldalam")
st.write("Üdv Áron weboldalán!")

nev = st.text_input("Hogy hívnak?")
if nev:
    st.write("Szia, " + nev + "! Jó, hogy itt vagy.")

szam = st.slider("Válassz számot:", 0, 10000)
st.write("A szam duplaja: ", szam*2)