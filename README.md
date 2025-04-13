# Krishna's Resume-Based RAG Chatbot 🤖

A small project where I combined **LangChain**, **FAISS Vector Store**, and **Gemini 1.5 Pro** to create a chatbot that answers questions about *me* — Krishna Tyagi — based on a knowledge base built from my resume!

---

## 🔧 Components

### 1. **Knowledge Base Creation**
- Used `TextLoader` to load my personal details from a `.txt` file.
- Embedded the data into vector representations using HuggingFace's `instructor-large` model.
- Stored the vectors using `FAISS` for efficient semantic search.

### 2. **Retrieval-Augmented Generation (RAG)**
- Retrieved the top relevant pieces of context using FAISS.
- Used a custom prompt template to guide the LLM.
- Passed the final context-question combo to **Gemini 1.5 Pro** for a human-like, context-aware answer.

### 3. **Streamlit Frontend**
- A simple Streamlit interface to ask questions and display answers.
- Added a button to create/update the knowledge base on demand.

---

## 🤖 Usage
```bash
pip install -r requirements.txt
streamlit run app.py
```
1. Click **Create Knowledge Base** to process the `krishna_profile.txt` file.
2. Type your question about Krishna in the input box.
3. The chatbot responds using the power of Gemini + FAISS.

---

## 🚀 Why I Built This
- Learn the practical flow of RAG systems from embedding to LLM querying.
- Experiment with `LangChain` integration using real-world context.
- Challenge myself to make an AI agent that can answer questions about me, powered by my own structured data!

---

## 🚫 Hosting Status
Originally planned to integrate this chatbot as a popup on my portfolio website.

⚠ Due to **storage constraints** on deployment platforms like Railway (large model dependencies), I couldn’t deploy it for now.

But I’m keeping this idea on hold — and will surely revisit once I explore better deployment solutions!

---

## 🌟 Tech Stack
- LangChain
- HuggingFace `instructor-large` Embeddings
- FAISS Vector Store
- Gemini 1.5 Pro (via Google AI)
- Streamlit

---

> Feel free to explore or fork this mini project! I built this to both learn and share the possibilities of combining structured personal data with powerful LLMs.

---
