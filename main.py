import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- SAFETY FILTER ----------------
def is_sensitive_query(query):
    keywords = ["suicide", "self harm", "overdose", "chest pain"]
    return any(k in query.lower() for k in keywords)

def safe_response():
    return "⚠️ Please consult a doctor immediately."

# ---------------- PROMPT ----------------
def build_prompt(user_input):
    return f"""
You are a helpful medical assistant.
Give simple health information only.

Question:
{user_input}
"""

# ---------------- MAIN FUNCTION ----------------
def ask_health_question(user_input):

    if is_sensitive_query(user_input):
        return safe_response()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": build_prompt(user_input)}]
    )

    return response.choices[0].message.content