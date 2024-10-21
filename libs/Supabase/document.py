from schemas.job_description import ENGLISH_LEVEL_ENUM
from libs.Supabase.auth import create_supabase_client

supabase = create_supabase_client()


def search_documents_by_candidate_ids(candidate_ids, page=1, page_size=100):
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

    resume_ids = [resume["id"] for resume in resumes["data"]]

    response = (
        supabase.from_("document")
        .select(
            "id, metadata, page_content, resume_id",
            count="exact",
        )
        .in_("resume_id", resume_ids)
        .execute()
    )

    documents = response.data
    total_count = response.count

    return {
        "total_count": total_count,
        "page": page,
        "page_size": page_size,
        "documents": documents,
    }
