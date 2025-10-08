import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mynterress", page_icon="🎬", layout="wide")

# ======================
# Sessão do usuário
# ======================
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

# ======================
# Sidebar como menu
# ======================
if st.session_state["usuario"]:
    st.sidebar.title(f"Olá, {st.session_state['usuario']['nome']}!")
    pagina = st.sidebar.radio("Menu", [
        "Perfil",
        "Reviews",
        "Comentários",
        "Pesquisa"  # será detectada automaticamente
    ])

    # Redireciona para as páginas usando o nome exato detectado pelo Streamlit
    if pagina == "Perfil":
        st.switch_page("02_perfilUsuario")
    elif pagina == "Reviews":
        st.switch_page("03_telaReviews")
    elif pagina == "Comentários":
        st.switch_page("04_Comentarios")
    elif pagina == "Pesquisa":
        st.switch_page("05_telaPesquisa")  # nome sem extensão


else:
    # Usuário não logado → mostrar landing + botão para login
    st.title("Mynterress")
    st.write("Uma rede social para mostrar aos outros seus interesses em diferentes formatos de mídia")

    if st.button("Comece agora mesmo!"):
        st.switch_page("01_Login")
