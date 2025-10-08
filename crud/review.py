from supabase_client import supabase

def criar_review(texto, nota, fk_id_usuario, fk_id_midia):
    return supabase.rpc(
        "criar_review",
        {"p_texto": texto, "p_nota": nota, "p_fk_id_usuario": fk_id_usuario, "p_fk_id_midia": fk_id_midia}
    ).execute().data

def atualizar_review(id_review, texto, nota):
    return supabase.rpc(
        "atualizar_review",
        {"p_id_review": id_review, "p_texto": texto, "p_nota": nota}
    ).execute

def deletar_review(id_review):
    return supabase.rpc(
        "deletar_review",
        {"p_id_review": id_review}
    ).execute().data

def listar_reviews():
    return supabase.rpc("listar_reviews").execute().data