import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. ..."
            "2. Upload an IMG, JPEG, or PNG file📄\n"
            "3. Ask a question about the document💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖MediGuard allows you to upload healthcare bills and claims"
            " to identify potential error or fraud."
        )
        st.markdown(
            "Powered by unsupervised machine learning"
            " trained with healthcare billing data."
            " MediGuard autonomously identifies suspicious patterns"
            " and anomalies in medical bills and reports cost accuracy."
        )
        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        #faq()