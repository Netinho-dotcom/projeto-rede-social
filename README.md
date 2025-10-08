# 🎬 Rede Social de Mídia

Uma aplicação web desenvolvida com **Streamlit (frontend)** e **Supabase (backend)** que funciona como uma **rede social de reviews de mídias** — onde usuários podem criar contas, avaliar filmes, séries, livros e jogos, e interagir por meio de comentários.

---

## 🚀 **Funcionalidades Principais**

- 👤 Cadastro e login de usuários  
- 📝 Criação e visualização de *reviews* (avaliações)  
- 💬 Sistema de comentários  
- ❤️ Likes em reviews  
- 🔍 Pesquisa avançada por usuários e reviews (com filtros por nome, gênero e tipo de mídia)  
- 📊 Interface moderna e responsiva com **Streamlit**

---

## 🧠 **Tecnologias Utilizadas**

| Camada | Tecnologia | Descrição |
|--------|-------------|-----------|
| Frontend | **Streamlit** | Interface web interativa e dinâmica |
| Backend | **Supabase** | Gerenciamento do banco de dados e autenticação |
| Banco de Dados | **PostgreSQL (via Supabase)** | Armazenamento dos dados de usuários, mídias, reviews e comentários |
| Linguagem | **Python 3.13+** | Lógica da aplicação e integração com o Supabase |

---

## 🧩 **Modelo Lógico do Banco de Dados (Mermaid)**

```mermaid
erDiagram
    USUARIO {
        int id_usuario PK
        varchar nome
        varchar email
        int idade
        text bio
    }

    GENERO {
        int id_genero PK
        varchar nome
    }

    MIDIA {
        int id_midia PK
        varchar titulo
        varchar tipo
        text descricao
        varchar capa_url
        date ano_lancamento
    }

    MIDIA_GENERO {
        int id_midia_genero PK
        int fk_id_midia FK
        int fk_id_genero FK
    }

    REVIEW {
        int id_review PK
        int fk_id_usuario FK
        int fk_id_midia FK
        varchar titulo
        int nota
        text texto
        int likes
    }

    COMENTARIO {
        int id_comentario PK
        int fk_id_usuario FK
        int fk_id_review FK
        text texto
    }

    %% Relacionamentos
    USUARIO ||--o{ REVIEW : "realiza"
    REVIEW ||--o{ COMENTARIO : "recebe"
    USUARIO ||--o{ COMENTARIO : "faz"
    MIDIA ||--o{ REVIEW : "é avaliada em"
    MIDIA ||--o{ MIDIA_GENERO : "pertence"
    GENERO ||--o{ MIDIA_GENERO : "classifica"

```



## **Links:**

deploy:  https://projeto-rede-social-rwu4ftnrsgqkaqy9mkjag9.streamlit.app/perfilUsuario

vídeo de apresentação: https://youtu.be/WX1rw7S96P8
