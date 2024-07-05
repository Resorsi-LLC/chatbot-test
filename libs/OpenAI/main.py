from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY
from schemas.job_description import (
    job_description_schema,
    job_description_additional_options_schema,
)

openai_api_key = OPENAI_API_KEY


def infer_data_from_job_description(prompt):
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key, temperature=0.2)
    structured_llm = llm.with_structured_output(schema=job_description_schema)
    result = structured_llm.invoke(prompt)
    return result


def get_additional_options_from_job_description(prompt):
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key, temperature=0.5)
    structured_llm = llm.with_structured_output(
        schema=job_description_additional_options_schema
    )
    structured_llm.invoke(prompt)
    result = structured_llm.invoke(prompt)
    return result
