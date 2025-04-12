import streamlit as st
from langchain_helper import create_vector_db, generate_answer

st.title("Krishna's RAG Chatbot 🤖")

if st.button("Create Knowledge Base"):
    create_vector_db()
    st.success("Knowledge base created successfully!")

query = st.text_input("Ask something about Krishna:")

if query:
    response = generate_answer(query)
    st.header("Answer")
    st.write(response)
