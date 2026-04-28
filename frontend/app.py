import streamlit as st
import requests

st.set_page_config(page_title="AI Ad Generator")

st.title("🚀 AI Ad Generator")

backend_url = st.text_input("Backend URL", "http://localhost:8000")

business = st.text_input("Business Type")
audience = st.text_input("Target Audience")
product = st.text_input("Product")
platform = st.selectbox("Platform", ["Instagram", "YouTube", "Facebook"])

if st.button("Generate Ad"):
    res = requests.post(f"{backend_url}/generate_ad", json={
        "business_type": business,
        "audience": audience,
        "product": product,
        "platform": platform
    })

    if res.status_code == 200:
        st.success("Ad Generated")
        st.write(res.json()["ad"])
    else:
        st.error("Error generating ad")
