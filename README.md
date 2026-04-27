Health Chatbot (Task 4)

📌 Project Overview

This project is a \*\*General Health Query Chatbot\*\* built using a Large Language Model (LLM).  

It allows users to ask general health-related questions and receive simple, safe, and friendly responses.


The chatbot uses \*\*prompt engineering\*\*, \*\*safety filters\*\*, and a \*\*Streamlit-based UI\*\* to ensure a good user experience.

🎯 Objective

\- Build a chatbot using an LLM

\- Answer general health-related queries

\- Use prompt engineering for better responses

\- Implement safety filters to prevent harmful advice

\- Create a simple and interactive UI


\## 🛠️ Technologies Used

\- Python

\- Streamlit (Frontend UI)

\- Groq API (LLM backend)

\- LLaMA 3.1 8B Instant model

\- python-dotenv (for API key management)

\## 🤖 AI Model \& API Used



\### ✔ API Used:

\*\*Groq API\*\*



\### ✔ Model Used:

\*\*LLaMA 3.1 8B Instant\*\*

\## ❓ Why Groq API was used instead of OpenAI / Hugging Face?

Although the internship suggested:

\- OpenAI GPT-3.5

\- Hugging Face (Mistral-7B)


We selected \*\*Groq API\*\* for the following reasons:


\### ✔ Advantages of Groq:

\- Free to use (no billing required)

\- Very fast response time

\- Stable and reliable

\- Easy integration with Python

\- Supports modern LLMs like LLaMA 3.1

\### ❌ Why not OpenAI?

\- Requires paid API access

\- Needs billing setup (not ideal for students)


\### ❌ Why not Hugging Face?

\- Free API is often unstable (i was facing errors when doing projetc so that why i shifted)

\- Many models are unavailable or decommissioned

\- Frequent errors like:

&#x20; "Cannot POST /models/..."


\## 🛡️ Safety Features


This chatbot includes a \*\*rule-based safety filter\*\* to prevent harmful responses.

\### ✔ What it does:

\- Detects sensitive keywords:

&#x20; - overdose

&#x20; - suicide

&#x20; - chest pain

&#x20; - severe symptoms

\- Blocks unsafe queries

\- Shows a warning instead of generating AI response

\### ✔ Purpose:

To ensure the chatbot does NOT provide dangerous medical advice.

\## 💬 Features

\- AI-powered chatbot responses

\- Prompt engineering (friendly medical assistant behavior)

\- Safety filtering system

\- Chat-like UI using Streamlit

\- Suggested health questions

\- Clear chat functionality


\## 📁 Project Structure



