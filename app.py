import streamlit as st

st.title("Az első weboldalam")
st.write("Üdv Áron weboldalán!")

nev = st.text_input("Hogy hívnak?")
if nev:
    st.write("Szia, " + nev + "! Jó, hogy itt vagy.")

szam = st.slider("Válassz számot:", 0, 10000)
st.write("A szam duplaja: ", szam*2)

szam1 = st.number_input("Szám1: ")
szam2 = st.number_input("Szám2: ")
st.write("A szamok összege: ", szam1+szam2)