import streamlit as st


ss = st.session_state

ss.setdefault('contador', 0)

if st.button("Incrementar"):
    ss.contador += 1
    

tab1, tab2, tab3 = st.tabs([":cat: Cat", ":dog: Dog", ":owl: Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    c1, c2 = st.columns(2)
    if c1.button("Festejar!"):
        st.balloons()
    c2.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    