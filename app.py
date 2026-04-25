import streamlit as st
from main import ask_health_question

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Health Chatbot", page_icon="🩺", layout="centered")

# ---------------- TITLE ----------------
st.title("🩺 Health Chatbot")
st.caption("AI-powered medical assistant (for general information only)")

# ---------------- SAFETY NOTICE ----------------
st.warning("⚠️ This chatbot does NOT provide medical diagnosis. Always consult a doctor for medical issues.")

# ---------------- SESSION STATE (CHAT HISTORY) ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR FEATURES ----------------
st.sidebar.title("⚙️ Options")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []

st.sidebar.markdown("### 💡 Suggested Questions")

suggestions = [
    "What causes fever?",
    "Is paracetamol safe for children?",
    "What is a sore throat?",
    "Symptoms of flu"
]

for s in suggestions:
    if st.sidebar.button(s):
        user_input = s

        response = ask_health_question(user_input)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# ---------------- INPUT ----------------
user_input = st.text_input("Ask your health question:")

if st.button("Ask") and user_input:

    with st.spinner("🧠 Thinking..."):
        response = ask_health_question(user_input)

    # save chat
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# ---------------- DISPLAY CHAT ----------------
for role, msg in st.session_state.chat_history:

    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
        st.markdown("---")