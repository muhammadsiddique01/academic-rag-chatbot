import streamlit as st
from rag import ask

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Football Strategy RAG Chatbot",
    page_icon="⚽",
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
st.sidebar.title("📌 Squad Strategy Overview")
st.sidebar.write("""
**Football-Themed Academic RAG Chatbot**

This system blends **computer science concepts** with **football tactics**
to make learning simple, exam-oriented, and memorable.

🔹 Definitions → *Rules of the Game*  
🔹 Concepts → *Team Tactics*  
🔹 Examples → *Match Day Scenarios*  

📚 Powered by **Retrieval-Augmented Generation (RAG)**  
⚙️ Local document retrieval + LLaMA (Groq API)
""")

st.sidebar.title("⚽ Squad Member Profile")
st.sidebar.write("""
### 🧠 The Tactical Analyst  
**Name:** Tabin Sheikh  

**Role:** Central Midfielder / Playmaker  
*(The Engine Room)*

**Training Drills (Course Load):**
- On-Field Communication  
- Tactical Blueprint (Compiler Construction)  
- Defensive Guarding (Information Security)  
- Total Football (Parallel & Distributed Computing)

**Major Trophy (FYP):**
- **Project:** VacciTrack FC  
- **Specialization:** Sports Science & Player Health  

**Career Goal:**  
🎯 Head of Performance Analysis  
(Data Analytics & AI for match prediction)
""")

st.sidebar.write("---")

st.sidebar.write("""
### 🏟️ The Club Director  
**Name:** Muhammad Zaahir  

**Role:** Club President / Sporting Director

**Training Drills (Course Load):**
- Boardroom Communication  
- League Regulations  
- Financial Fair Play (Information Security)  
- Global Scouting Networks

**Major Trophy (FYP):**
- **Domain:** Football Transfer Market Analytics  

**Career Goal:**  
💼 Football Mogul  
(Entrepreneurship, club ownership & market analysis)
""")

# ================= MAIN UI =================
st.markdown(
    '<div class="title">⚽ Football Strategy RAG Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn Computer Science concepts through Football Tactics, Match Scenarios, and Game Strategies'
    '</div>',
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    question = st.text_input(
        "🎯 Ask your tactical (academic) question",
        placeholder="e.g., Explain compiler phases like a football manager’s playbook"
    )

    if question:
        with st.spinner("📊 Analyzing tactics and generating match-winning insights..."):
            answer = ask(question)

        st.markdown("### ✅ Tactical Answer")
        st.write(answer)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(
    '<div class="footer">'
    '⚽ Football Strategy RAG Chatbot | '
    'Tactical Analyst: Tabin Sheikh | '
    'Club Director: Muhammad Zaahir | '
    'Built with Streamlit & RAG'
    '</div>',
    unsafe_allow_html=True
)
