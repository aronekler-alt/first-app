import streamlit as st
import json

st.title("Naplóm")
if "bejegyzesek" not in st.session_state:
    st.session_state.bejegyzesek = []

# Korábbi napló betöltése
feltoltott = st.file_uploader("Napló betöltése", type="json")
if feltoltott is not None:
    st.session_state.bejegyzesek = json.load(feltoltott)

# Új bejegyzés
uj = st.text_input("Mi történt ma?")
if st.button("Hozzáadás"):
    st.session_state.bejegyzesek.append(uj)

# Megjelenítés
for b in st.session_state.bejegyzesek:
    st.write("- " + b)

# Mentés fájlba
adat = json.dumps(st.session_state.bejegyzesek)
st.download_button("Napló mentése", adat, "naplo.json")
