import streamlit as st
from supabase_client import supabase

if "usuario" not in st.session_state:
    st.warning("Você precisa fazer login primeiro.")
    st.switch_page("pages/01_login.py")

usuario = st.session_state["usuario"]

st.title(f"Perfil de {usuario['nome']}")

st.write(f"📧 Email: {usuario['email']}")
st.write(f"🎂 Idade: {usuario['idade']}")
st.write(f"📝 Bio: {usuario['bio']}")

if st.button("Minhas Reviews"):
    st.switch_page("pages/03_telaReviews.py")

if st.button("Sair"):
    st.session_state.clear()
    st.switch_page("pages/01_login.py")
