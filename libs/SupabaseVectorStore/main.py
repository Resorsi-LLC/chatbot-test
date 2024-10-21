from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from libs.Supabase.auth import create_supabase_client
from config import OPENAI_API_KEY

openai_api_key = OPENAI_API_KEY

supabase = create_supabase_client()
embeddings = OpenAIEmbeddings(api_key=openai_api_key, model="text-embedding-ada-002")


def parse_document(doc):
    metadata = doc.metadata
    page_content = doc.page_content

    loc = metadata.get("loc", "No location")
    file_name = metadata.get("file_name", "No file name")
    candidate_number = metadata.get("candidate_number", "No candidate number")
    trade_of_service = metadata.get("trade_of_service", "No trade of service")
    candidate_id = metadata.get("candidate_id", "No candidate ID")

    return {
        "loc": loc,
        "file_name": file_name,
        "candidate_id": candidate_id,
        "candidate_number": candidate_number,
        "trade_of_service": trade_of_service,
        "page_content": page_content,
    }


def retrieve_candidate_documents(prompt, document_ids=None, max_docs=10):
    vector_store = SupabaseVectorStore(
        client=supabase,
        embedding=embeddings,
        table_name="document",
        query_name="match_candidate_embeddings",
    )

    matched_docs = vector_store.similarity_search(
        query=prompt,
        filter={"id": document_ids},
        k=max_docs,
    )

    return {
        "count": len(matched_docs),
        "documents": [parse_document(doc) for doc in matched_docs],
    }
