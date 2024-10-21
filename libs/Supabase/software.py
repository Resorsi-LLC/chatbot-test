from libs.Supabase.auth import create_supabase_client

supabase = create_supabase_client()


def get_softwares():

    response = (
        supabase.table("software").select("name").order("name", desc=False).execute()
    )

    softwares = [item["name"] for item in response.data]

    return softwares


def search_softwares(software_names):
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
