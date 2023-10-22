import streamlit as st

def dataTab():
    submitted = False
    buttonState = False
    uploaded_file = None
    provider_first = ""
    provider_last = ""
    submitted_charge = 0
    has_med = ''
    med_payment = 0
    HCPCS = 0

    provider_firstI = ""
    provider_lastI = ""
    submitted_chargeI = 0
    has_medI = ''
    med_paymentI = 0
    HCPCSI = 0
    uploadTab, inputTab = st.tabs(["Upload","Info"])

    st.markdown(
        """
        <style>
            /* Center the text within the button */
            .stButton > button span {
                display: flex;
                align-items: center;
                justify-content: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )  
    with uploadTab:
        uploaded_file = st.file_uploader(
            "Upload a png, pdf, or jpeg file",
            type=["png", "pdf"]
        )
        if uploaded_file != None:
            left, right = st.columns([6,1])
            with right:    
                if st.button("Scan"):
                    buttonState = True
                    uploaded_file = None
                    #provider_firstI, provider_lastI, submitted_chargeI, has_medI, med_paymentI, HCPCS = UPLOAD
                    
    with inputTab:
        with st.form("Information"):
            if not buttonState:
                st.write("Information")
                provider_first = st.text_input("Provider First Name")
                provider_last = st.text_input("Provider Last Name")
                submitted_charge = st.number_input("Total Cost")
                st.write("Prescribed Medication")
                has_med = st.checkbox('Yes')
                med_payment = st.number_input("Medicare Payment")
                HCPCS = st.number_input("Medicare Payment")
                if st.form_submit_button():
                    with open("form_submit_state.txt", "w") as file:
                        file.write("pressed")
            else:
                st.write("Information")
                provider_first = st.text_input("Provider First Name", provider_firstI)
                provider_last = st.text_input("Provider Last Name", provider_lastI)
                submitted_charge = st.number_input("Total Cost", submitted_chargeI)
                st.write("Has Medicare")
                has_med = st.checkbox('Yes')
                med_payment = st.number_input("Medicare Payment", med_paymentI)
                HCPCS = st.number_input("Medicare Payment", HCPCSI)
                if st.form_submit_button():
                    with open("form_submit_state.txt", "w") as file:
                        file.write("pressed")
    return provider_first, provider_last, submitted_charge, has_med, med_payment, HCPCS
