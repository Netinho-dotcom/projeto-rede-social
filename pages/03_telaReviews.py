import streamlit as st
from supabase_client import supabase

if "usuario" not in st.session_state:
    st.warning("Você precisa fazer login primeiro.")
    st.switch_page("pages/01_login.py")

usuario = st.session_state["usuario"]

st.title("Minhas Reviews 🎬")

# Buscar as reviews do usuário
reviews = supabase.table("review").select("*").eq("fk_id_usuario", usuario["id_usuario"]).execute().data

if reviews:
    for r in reviews:
        st.subheader(r.get("titulo", "Sem título"))
        st.write(r["texto"])
        st.write(f"⭐ Nota: {r['nota']}")
        st.write("---")
        if st.button(f"Ver comentários da review {r['id_review']}", key=r["id_review"]):
            st.session_state["id_review"] = r["id_review"]
            st.switch_page("pages/04_telaComentarios.py")
else:
    st.info("Você ainda não possui reviews.")

# Criar nova review
st.subheader("Criar nova review")
texto = st.text_area("texto")
nota = st.slider("Nota", 0, 10, 5)

if st.button("Salvar Review"):
    supabase.table("review").insert({
        "texto": texto,
        "nota": nota,
        "fk_id_usuario": usuario["id_usuario"]
    }).execute()
    st.success("Review criada com sucesso!")
    st.rerun()

if st.button("Voltar ao perfil"):
    st.switch_page("pages/02_perfilUsuario.py")
