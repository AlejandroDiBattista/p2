import streamlit as st

st.title("Saludador...")
nombre = st.text_input("Escribe tu nombre")
edad = st.number_input("Escribe tu edad", min_value=18, max_value=65, step=1)   
nacimiento = st.date_input("Fecha de nacimiento")
if nombre:
    st.header(f"Hola, {nombre} tenes {edad} años!")
else:
    st.error("Por favor, ingresa tu nombre.")