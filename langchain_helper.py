from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# Embedding model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "vectorstore_index"

def create_vector_db():
    loader = TextLoader(file_path='data/krishna_profile.txt')
    documents = loader.load()
    vectordb = FAISS.from_documents(documents, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(
        vectordb_file_path,
        instructor_embeddings,
        allow_dangerous_deserialization=True  # safe if you're loading your own file!
    )
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """You are a helpful AI assistant. Use the following context to answer the question.
If the answer is not found in the context, reply: "I don't know."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    return retriever, prompt

def generate_answer(question):
    retriever, prompt = get_qa_chain()
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.format(context=context, question=question)

    response = model.generate_content(final_prompt)
    return response.text

if __name__ == "__main__":
    create_vector_db()
    answer = generate_answer("Tell me about Krishna's projects.")
    print(answer)
