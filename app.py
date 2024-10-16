import streamlit as st

from libs.OpenAI.main import (
    openai_api_key,
    infer_data_from_job_description,
    get_additional_options_from_job_description,
)
from libs.Supabase.candidate import search_candidates
from schemas.job_description import (
    TRADE_OF_SERVICE_ENUM,
    YEARS_OF_EXPERIENCE_ENUM,
    ENGLISH_LEVEL_ENUM,
)
from utils.parse_job_description import parse_inferred_data_from_job_description

st.title("Job Description Chatbot")


if openai_api_key:
    search = "I am looking for a Sr. frontend developer with over three years of experience in Next.js, TypeScript, Azure, and AI."
    prompt = st.text_area(
        "Enter the job description:", placeholder=search, value=search
    )

    if st.button("Generate"):
        if prompt:
            with st.spinner("Inferring Data..."):
                inferred_data = infer_data_from_job_description(prompt)

                desired_roles = "', '".join(map(str, inferred_data["desired_roles"]))
                years_of_experience = "', '".join(
                    map(str, inferred_data["years_of_experience"])
                )
                technologies = "', '".join(map(str, inferred_data["technologies"]))

                job_desc_prompt = f"The desired role is '{desired_roles}', the years of experience are {years_of_experience} and the technologies are '{technologies}'."
                additional_options = get_additional_options_from_job_description(
                    job_desc_prompt
                )

                st.session_state.inferred_data = (
                    parse_inferred_data_from_job_description(inferred_data)
                )
                st.session_state.additional_options = additional_options

        else:
            st.error("Please enter a job description.")
else:
    st.warning("Please enter your OpenAI API key.")


if "inferred_data" and "additional_options" in st.session_state:
    trade_of_services = st.session_state.inferred_data.get("trade_of_service", [])
    years_of_experience = st.session_state.inferred_data.get("years_of_experience", [])
    english_level = st.session_state.inferred_data.get("english_level", [])
    desired_roles = st.session_state.inferred_data.get("desired_roles", [])
    technologies = st.session_state.inferred_data.get("technologies", [])

    inferred_and_additional_desired_roles = (
        desired_roles + st.session_state.additional_options.get("desired_roles", [])
    )
    inferred_and_additional_technologies = (
        technologies + st.session_state.additional_options.get("technologies", [])
    )

    selected_trade_of_services = st.multiselect(
        "What trade of service should the candidate have?",
        TRADE_OF_SERVICE_ENUM,
        trade_of_services,
    )
    selected_years_of_experience = st.multiselect(
        "How many years of experience should the candidate have?",
        YEARS_OF_EXPERIENCE_ENUM,
        years_of_experience,
    )
    selected_english_levels = st.multiselect(
        "What Minimum English level should the candidate have?",
        ENGLISH_LEVEL_ENUM,
        english_level,
        max_selections=1,
    )

    selected_desired_roles = st.multiselect(
        "What desired role should the candidate have?",
        inferred_and_additional_desired_roles,
        desired_roles,
    )
    selected_technologies = st.multiselect(
        "What technologies should the candidate be proficient in?",
        inferred_and_additional_technologies,
        technologies,
    )

    if st.button("Search"):
        with st.spinner("Searching..."):
            candidates = search_candidates(
                selected_trade_of_services,
                selected_years_of_experience,
                selected_english_levels,
            )

            st.write(candidates)
