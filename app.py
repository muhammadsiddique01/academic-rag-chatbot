import streamlit as st
from rag import ask

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("📚 Academic RAG Chatbot")
st.write("Ask questions from your lecture PDFs and PPTs")

query = st.text_input("Enter your question")

if query:
    with st.spinner("Thinking..."):
        answer = ask(query)
    st.subheader("Answer")
    st.write(answer)
