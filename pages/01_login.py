import streamlit as st
from supabase_client import supabase
from crud import usuario  # Funções do CRUD

# ====== CONFIGURAÇÃO DA PÁGINA ======
st.set_page_config(
    page_title="Login - Mynterress",
    page_icon="🔐",
    layout="wide",
)

# ====== ESCONDER BARRA LATERAL ======
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stToolbar"] {display: none;}
.stApp {background-color: #121212; color: #FFFFFF; font-family: 'Poppins', sans-serif;}
h1 {color: #00ADB5; text-align: center;}
div.stButton > button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.8em 1.5em;
    font-weight: 600;
    width: 200px;
}
div.stButton > button:hover {background-color: #08C5D1; transform: scale(1.05);}
label, p {color: #EEEEEE; font-size: 1em;}
</style>
""", unsafe_allow_html=True)

# ====== TÍTULO ======
st.markdown("<h1>Login 👤</h1>", unsafe_allow_html=True)

# ====== Inicializa estado ======
if "cadastro" not in st.session_state:
    st.session_state["cadastro"] = False

# ====== FORMULÁRIO DE CADASTRO ======
if st.session_state["cadastro"]:
    st.markdown("<h2>Cadastro</h2>", unsafe_allow_html=True)
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    idade = st.number_input("Idade", min_value=1, max_value=120)
    bio = st.text_area("Bio (opcional)")

    if st.button("Cadastrar"):
        # Chama função do CRUD
        success = usuario.criar_usuario(nome, email, idade, bio)
        if success:
            st.success(f"Usuário {nome} cadastrado com sucesso!")
            st.session_state["usuario"] = {"nome": nome, "email": email, "idade": idade, "bio": bio}
            st.session_state["cadastro"] = False
        else:
            st.error("Usuário já existe ou ocorreu um erro.")

    if st.button("Já possui conta? Login"):
        st.session_state["cadastro"] = False

# ====== FORMULÁRIO DE LOGIN ======
else:
    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Entrar"):
        response = usuario.login_usuario(nome, email)
        if response:
            st.session_state["usuario"] = response
            st.success(f"Bem-vindo, {nome}!")
            st.switch_page("pages/02_perfilUsuario.py")
        else:
            st.error("Usuário não encontrado. Verifique nome e email.")

    # Link para cadastro
    if st.button("Cadastre-se"):
        st.session_state["cadastro"] = True
