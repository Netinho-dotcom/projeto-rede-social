import streamlit as st
from supabase_client import supabase

if "usuario" not in st.session_state or "id_review" not in st.session_state:
    st.warning("Você precisa acessar uma review primeiro.")
    st.switch_page("pages/03_telaReviews.py")

usuario = st.session_state["usuario"]
id_review = st.session_state["id_review"]

st.title("Comentários 💬")

# Buscar comentários da review
comentarios = supabase.table("comentario").select("*").eq("fk_id_review", id_review).execute().data

if comentarios:
    for c in comentarios:
        st.write(f"👤 {c['fk_id_usuario']} disse:")
        st.write(c["texto"])
        st.write("---")
else:
    st.info("Ainda não há comentários nesta review.")

# Novo comentário
st.subheader("Adicionar um comentário")
texto = st.text_area("Comentário")

if st.button("Enviar comentário"):
    supabase.table("comentario").insert({
        "fk_id_review": id_review,
        "fk_id_usuario": usuario["id_usuario"],
        "texto": texto
    }).execute()
    st.success("Comentário adicionado!")
    st.rerun()

if st.button("Voltar às reviews"):
    st.switch_page("pages/03_telaReviews.py")
