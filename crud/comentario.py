from supabase_client import supabase

def criar_comentario(texto, fk_id_review, fk_id_usuario):
    return supabase.rpc(
        "criar_comentario",
        {"p_texto": texto, "p_fk_id_review": fk_id_review, "p_fk_id_usuario": fk_id_usuario}
    ).execute().data

def atualizar_comentario(id_comentario, texto):
    return supabase.rpc(
        "atualizar_comentario",
        {"p_id_comentario": id_comentario, "p_texto": texto}
    ).execute().data

def deletar_comentario(id_comentario):
    return supabase.rpc(
        "deletar_comentario",
        {"p_id_comentario": id_comentario}
    ).execute().data

def listar_comentarios():
    return supabase.rpc("listar_comentarios").execute().data
