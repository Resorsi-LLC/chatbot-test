from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


def search_candidates(
    trade_of_service, years_of_experience, english_level, page=1, page_size=100
):
    print("trade_of_service: ", trade_of_service)
    print("years_of_experience: ", years_of_experience)
    print("english_level: ", english_level)
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    start = (page - 1) * page_size
    end = page * page_size - 1

    response = (
        supabase.from_("candidate")
        .select("candidate_number, first_name, last_name", count="exact")
        .range(start, end)
        .in_("trade_of_service", trade_of_service)
        .in_("years_of_experience", years_of_experience)
        .in_("english_level", english_level)
        .execute()
    )

    candidates = response.data
    total_count = response.count

    return {
        "total_count": total_count,
        "candidates": candidates,
        "page": page,
        "page_size": page_size,
    }
