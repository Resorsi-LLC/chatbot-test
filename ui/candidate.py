import streamlit as st


def generate_zoho_link(zoho_id):
    return f"https://crm.zoho.com/crm/org824437383/tab/CustomModule1/{zoho_id}/"


def create_candidate_card(candidates):
    st.markdown(f"## {len(candidates)} unique candidates retrieved")

    for index, candidate in enumerate(candidates, start=1):
        st.write("---")
        with st.container():
            first_name = candidate.get("first_name", "N/A")
            last_name = candidate.get("last_name", "N/A")
            candidate_number = candidate.get("candidate_number", "N/A")
            zoho_id = candidate.get("zoho_id", "")

            trade_of_service = candidate.get("trade_of_service", "N/A")
            location = candidate.get("location", "N/A")
            years_of_experience = candidate.get("years_of_experience", "N/A")
            english_level = candidate.get("english_level", "N/A")
            supabase_id = candidate.get("id", "N/A")

            resume_info = candidate.get("resume", {}).get("resume_personal_info", None)
            if resume_info:
                current_role = resume_info.get("current_role", {}).get("name", "N/A")
            else:
                current_role = "N/A"

            st.markdown(
                f"### [{index}. {first_name} {last_name} {'(' + candidate_number + ')'}]({generate_zoho_link(zoho_id)})"
            )

            st.write(f"**Supabase Candidate id:** {supabase_id}")
            st.write(f"**Trade of Service:** {trade_of_service}")
            st.write(f"**Current Role:** {current_role}")
            st.write(f"**Location:** {location}")
            st.write(f"**Years of experience:** {years_of_experience}")
            st.write(f"**English Level:** {english_level}")

            documents = candidate.get("resume", {}).get("document", [])
            full_content = "\n\n".join(
                doc.get("content", "No content available") for doc in documents
            )

            if "------------------------------" in full_content:
                full_content = full_content.split("------------------------------", 1)[
                    1
                ].lstrip("\n")

            with st.expander("See resume details"):
                st.write(full_content or "No resume details available.")
