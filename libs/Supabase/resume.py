from schemas.job_description import ENGLISH_LEVEL_ENUM
from libs.Supabase.auth import create_supabase_client

supabase = create_supabase_client()


def get_resume(resume_id):
    resume = supabase.from_("resume").select("*").eq("id", resume_id).single().execute()

    return resume


def get_resumes_by_candidate_ids(candidate_ids, page=1, page_size=100):
    start = (page - 1) * page_size
    end = page * page_size - 1

    resumes = (
        supabase.from_("resume")
        .select(
            "candidate_id",
            count="exact",
        )
        .range(start, end)
        .in_("candidate_id", candidate_ids)
        .execute()
    )

    return {
        "total_count": resumes["count"],
        "page": page,
        "page_size": page_size,
        "resumes": resumes["data"],
    }
