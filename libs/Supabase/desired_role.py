from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


def get_roles():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (
        supabase.table("current_role")
        .select("name")
        .order("name", desc=False)
        .execute()
    )

    roles = [item["name"] for item in response.data]

    return roles
