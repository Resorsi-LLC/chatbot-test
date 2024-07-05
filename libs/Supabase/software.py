from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


def get_softwares():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (
        supabase.table("software").select("name").order("name", desc=False).execute()
    )

    softwares = [item["name"] for item in response.data]

    return softwares


def search_softwares():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (
        supabase.table("software")
        .select("name")
        .order("name", desc=False)
        .text_search("name", "HTML")
        .execute()
    )

    softwares = [item["name"] for item in response.data]

    return softwares
