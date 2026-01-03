
import streamlit as st
from rag import ask

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Academic RAG Chatbot",
    page_icon="📚",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #f6f9fc, #e9eff5);
}
.title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 5px;
}
.subtitle {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 30px;
}
.card {
    background: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
}
.footer {
    text-align: center;
    color: gray;
    font-size: 0.9rem;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("📌 Project Overview")
st.sidebar.write("""
**Academic RAG Chatbot**

This system uses **Retrieval-Augmented Generation (RAG)** to answer
questions from lecture **PDFs, PPTs, and profile data**.

🔹 Retrieval: Local document search  
🔹 Generation: LLaMA via Groq API  
🔹 Deployment: Streamlit Cloud
""")

st.sidebar.title("👥 Project Members")
st.sidebar.write("""
**Muhammad Siddique**  
BS Computer Science  
📌 **FYP: Stock Exchange Analysis**

---

**Muhammad Waseeq Khan**  
BS Computer Science  
🎯 **Aspiring Data Scientist**
""")

# ================= MAIN UI =================
st.markdown('<div class="title">📚 Academic RAG Chatbot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Ask questions from your lecture PDFs, PPTs, and academic material</div>',
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    question = st.text_input(
        "🔍 Enter your question",
        placeholder="e.g., What is left recursion in compiler construction?"
    )

    if question:
        with st.spinner("Analyzing documents and generating answer..."):
            answer = ask(question)

        st.markdown("### ✅ Answer")
        st.write(answer)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(
    '<div class="footer">🚀 Academic RAG Chatbot | '
    'Developed by Muhammad Siddique & Muhammad Waseeq Khan | '
    'Deployed on Streamlit Cloud</div>',
    unsafe_allow_html=True
)
