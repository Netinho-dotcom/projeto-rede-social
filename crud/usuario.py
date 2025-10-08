from supabase_client import supabase

def criar_usuario(nome, email, idade, bio):
    return supabase.rpc(
        "criar_usuario",
        {"p_nome": nome, "p_email": email, "p_idade": idade, "p_bio": bio}
    ).execute().data

def atualizar_usuario(id_usuario, nome, email, idade, bio):
    return supabase.rpc(
        "atualizar_usuario",
        {"p_id_usuario": id_usuario, "p_nome": nome, "p_email": email, "p_idade": idade, "p_bio": bio}
    ).execute().data

def deletar_usuario(id_usuario):
    return supabase.rpc("deletar_usuario", {"p_id_usuario": id_usuario}).execute().data

def listar_usuarios():
    return supabase.rpc("listar_usuarios").execute().data


from supabase_client import supabase

def login_usuario(nome: str, email: str):
    """
    Verifica se o usuário existe no banco.
    Retorna o usuário se encontrado, ou None se não encontrado.
    """
    response = supabase.table("usuario").select("*").eq("nome", nome).eq("email", email).execute()
    if response.data:
        return response.data[0]
    return None
