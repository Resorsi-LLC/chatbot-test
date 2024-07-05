from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


def get_softwares():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (
        supabase.table("software").select("name").order("name", desc=False).execute()
    )

    softwares = [item["name"] for item in response.data]

    return softwares


def search_softwares(software_names):
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    softwares = []

    for name in software_names:
        response = (
            supabase.table("software")
            .select("name")
            .order("name", desc=False)
            .text_search("name", name, options={"type": "websearch"})
            .execute()
        )

        softwares.extend([item["name"] for item in response.data])

    return list(set(softwares))  # Remove duplicates
