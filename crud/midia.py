from supabase_client import supabase

def criar_midia(titulo, tipo, descricao, capa_url):
    return supabase.rpc(
        "criar_midia",
        {"p_titulo": titulo, "p_tipo": tipo, "p_descricao": descricao, "p_capa_url": capa_url}
    ).execute().data

def atualizar_midia(id_midia, titulo, tipo, descricao, capa_url):
    return supabase.rpc(
        "atualizar_midia",
        {"p_id_midia": id_midia, "p_titulo": titulo, "p_tipo": tipo, "p_descricao": descricao, "p_capa_url": capa_url}
    ).execute().data

def deletar_midia(id_midia):
    return supabase.rpc("deletar_midia", {"p_id_midia": id_midia}).execute().data

def listar_midias():
    return supabase.rpc("listar_midias").execute().data