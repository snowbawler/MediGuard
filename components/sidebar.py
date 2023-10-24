import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload an IMG, JPEG, or PNG file📄\n"
            "2. Scan and check Info tab for accuracy\n"
            "3. Submit and check for fraud💬\n"
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
        st.markdown("Made by [snowbawler](https://github.com/snowbawler)")
        st.markdown("---")

        #faq()