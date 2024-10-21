from schemas.job_description import ENGLISH_LEVEL_ENUM
from libs.Supabase.auth import create_supabase_client

supabase = create_supabase_client()


def get_candidates(candidate_ids):
    response = (
        supabase.from_("candidate")
        .select(
            "zoho_id, candidate_number, first_name, last_name, location, trade_of_service, years_of_experience, english_level, resume(link, document(id, content))",
            count="exact",
        )
        .in_("id", candidate_ids)
        .execute()
    )

    candidates = response.data
    total_count = response.count

    return {
        "total_count": total_count,
        "candidates": candidates,
    }


def search_candidates(
    trade_of_service, years_of_experience, english_level, page=1, page_size=100
):
    start = (page - 1) * page_size
    end = page * page_size - 1

    english_level_start_index = ENGLISH_LEVEL_ENUM.index(english_level[0])
    english_level_list = ENGLISH_LEVEL_ENUM[english_level_start_index:]

    response = (
        supabase.from_("candidate")
        .select(
            "candidate_number, first_name, last_name, resume(document(id))",
            count="exact",
        )
        .range(start, end)
        .in_("trade_of_service", trade_of_service)
        .in_("years_of_experience", years_of_experience)
        .in_("english_level", english_level_list)
        .execute()
    )

    candidates = response.data
    total_count = response.count

    return {
        "total_count": total_count,
        "page": page,
        "page_size": page_size,
        "candidates": candidates,
    }
