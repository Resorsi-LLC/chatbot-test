import streamlit as st


def generate_zoho_link(zoho_id):
    return f"https://crm.zoho.com/crm/org824437383/tab/CustomModule1/{zoho_id}/"


def create_candidate_card(candidates):
    st.markdown(f"## {len(candidates)} unique candidates found")

    for candidate in candidates:
        st.write("---")
        with st.container():
            st.markdown(
                f"### [{candidate['first_name']} {candidate['last_name']} {'(' + candidate['candidate_number'] + ')'}]({generate_zoho_link(candidate['zoho_id'])})"
            )

            st.write(f"**Location:** {candidate['location']}")
            st.write(f"**Trade of Service:** {candidate['trade_of_service']}")
            st.write(f"**Years of experience:** {candidate['years_of_experience']}")
            st.write(f"**English Level:** {candidate['english_level']}")

            full_content = "\n\n".join(
                doc["content"] for doc in candidate["resume"]["document"]
            )

            if "------------------------------" in full_content:
                full_content = full_content.split("------------------------------", 1)[
                    1
                ].lstrip("\n")

            with st.expander("Ver detalles del currículum"):
                st.write(full_content)
