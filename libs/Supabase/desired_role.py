from libs.Supabase.auth import create_supabase_client

supabase = create_supabase_client()


def get_roles():
    response = (
        supabase.table("current_role")
        .select("name")
        .order("name", desc=False)
        .execute()
    )

    roles = [item["name"] for item in response.data]

    return roles
