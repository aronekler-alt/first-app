import streamlit as st
class Allat:
    def __init__(self, nev):
        self.nev = nev
    def hang(self): 
        return "..."
class Kutya(Allat):
    def hang(self):
        return "Vau!"
class Macska(Allat):
    def hang(self):
        return "Miau!"
st.title("Kis állatkert")
if "allatok" not in st.session_state:
    st.session_state.allatok = []
nev = st.text_input("Az állat neve")
faj = st.radio("Milyen állat?", ["Kutya", "Macska"])
if st.button("Hozzáadás"):
    if faj == "Kutya":
        st.session_state.allatok.append(Kutya(nev))
else:
    st.session_state.allatok.append(Macska(nev))
st.write("Az állatkert lakói:")
for allat in st.session_state.allatok:
    st.subheader(allat.nev)
st.write("Hangja: " + allat.hang())
st.metric("Állatok száma", len(st.session_state.allatok))
