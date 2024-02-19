import streamlit as st

st.title('My first app')

frase = st.text_input("Insira a frase", "")

st.write(frase)
if (frase !=''):
    st.write("Possui {} letras".format(len(frase)))