import streamlit as st
from supabase_client import supabase

# ====== ESTILO ======
st.markdown("""
<style>
.stApp {font-family: 'Poppins', sans-serif; background-color: #121212; color: #FFFFFF;}
h1 {color: #00ADB5; text-align: center;}
.card {
    background-color: #1E1E1E; 
    padding: 15px; 
    border-radius: 10px; 
    margin-bottom: 10px;
}
.stButton > button {
    background-color: #00ADB5; color: white; border-radius: 10px; border: none;
    padding: 0.5em 1em; font-weight: 600;
}
.stButton > button:hover {background-color: #08C5D1; transform: scale(1.05);}
</style>
""", unsafe_allow_html=True)

st.title("Pesquisa 🔍")

# ====== TIPO DE PESQUISA ======
tipo_pesquisa = st.radio("Pesquisar por:", ["Usuários", "Reviews"], horizontal=True)

# ====== BARRA LATERAL COM FILTROS ======
with st.sidebar:
    st.header("Filtros Avançados")

    if tipo_pesquisa == "Usuários":
        nome_usuario = st.text_input("Nome do usuário")
        min_likes = st.slider("Número mínimo de likes nas reviews", 0, 100, 0)
    else:
        titulo_review = st.text_input("Título da review")
        generos = ["Todos"] + [g["nome"] for g in supabase.table("genero").select("*").execute().data]
        genero_review = st.selectbox("Gênero da review", generos)
        tipos_midia = ["Todos"] + [m["tipo"] for m in supabase.table("midia").select("tipo").execute().data]
        tipo_midia = st.selectbox("Tipo de mídia", tipos_midia)

# ====== PESQUISA POR USUÁRIOS ======
if tipo_pesquisa == "Usuários":
    if st.button("Pesquisar usuários"):
        query = supabase.table("usuario").select("*")
        if nome_usuario:
            query = query.ilike("nome", f"%{nome_usuario}%")
        usuarios = query.execute().data or []

        # Filtrar por likes
        if min_likes > 0:
            usuarios_filtrados = []
            for u in usuarios:
                reviews = supabase.table("review").select("likes").eq("fk_id_usuario", u["id_usuario"]).execute().data or []
                likes_total = sum([r.get("likes", 0) for r in reviews])
                if likes_total >= min_likes:
                    usuarios_filtrados.append(u)
            usuarios = usuarios_filtrados

        # Exibir resultados
        st.subheader("Resultados")
        if not usuarios:
            st.info("Nenhum usuário encontrado.")
        for u in usuarios:
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <strong>Nome:</strong> {u['nome']}<br>
                    <strong>Email:</strong> {u['email']}<br>
                    <strong>Idade:</strong> {u.get('idade', '-') }<br>
                    <strong>Bio:</strong> {u.get('bio', '-') }
                </div>
                """, unsafe_allow_html=True)

# ====== PESQUISA POR REVIEWS ======
else:
    if st.button("Pesquisar reviews"):
        query = supabase.table("review").select("*")
        if titulo_review:
            query = query.ilike("titulo", f"%{titulo_review}%")
        reviews = query.execute().data or []

        # Filtrar por gênero
        if genero_review != "Todos":
            reviews_filtrados = []
            for r in reviews:
                midia_generos = supabase.table("midia_genero").select("*").eq("fk_id_midia", r["fk_id_midia"]).execute().data or []
                generos_midia = []
                for mg in midia_generos:
                    g = supabase.table("genero").select("nome").eq("id_genero", mg["fk_id_genero"]).execute().data
                    if g:
                        generos_midia.append(g[0]["nome"])
                if genero_review in generos_midia:
                    reviews_filtrados.append(r)
            reviews = reviews_filtrados

        # Filtrar por tipo de mídia
        if tipo_midia != "Todos":
            reviews = [
                r for r in reviews
                if supabase.table("midia").select("tipo").eq("id_midia", r["fk_id_midia"]).execute().data[0]["tipo"] == tipo_midia
            ]

        # Exibir resultados
        st.subheader("Resultados")
        if not reviews:
            st.info("Nenhuma review encontrada.")
        for r in reviews:
            midia = supabase.table("midia").select("*").eq("id_midia", r["fk_id_midia"]).execute().data[0]
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <strong>Título:</strong> {r['titulo']}<br>
                    <strong>Mídia:</strong> {midia['titulo']} ({midia['tipo']})<br>
                    <strong>Likes:</strong> {r.get('likes', 0)}<br>
                    <strong>Comentário:</strong> {r.get('texto', '-') }
                </div>
                """, unsafe_allow_html=True)
