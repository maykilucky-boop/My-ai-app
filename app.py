import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="আমার পার্সোনাল AI", page_icon="🤖")
st.title("🤖 আমার পার্সোনাল AI")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("কী সাহায্য করতে পারি?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
except Exception as e:
    st.error("API Key সেটআপ করা হয়নি। Streamlit Secrets এ গিয়ে API Key যোগ করুন।")
  
