from langchain_chroma import Chroma
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
from datetime import datetime
import streamlit as st
import json
import os

load_dotenv()

model = os.getenv('LLM_MODEL', 'meta-llama/Meta-Llama-3.1-405B-Instruct')
rag_directory = os.getenv('DIRECTORY', 'meeting_notes')

@st.cache_resource
def get_local_model():
  return HuggingFaceEndpoint(
    repo_id=model,
    task="text-generation",
    max_new_tokens=1024,
    do_sample=False
  )

  # If you want to run the model absolutely locally - VERY resource intense!
  # return HuggingFacePipeline.from_model_id(
  #     model_id=model,
  #     task="text-generation",
  #     pipeline_kwargs={
  #         "max_new_tokens": 1024,
  #         "top_k": 50,
  #         "temperature": 0.4
  #     },
  # )

llm = get_local_model()

def load_documents(directory):
    # Load the PDF or txt documents from the directory
    loader = DirectoryLoader(directory)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    return docs


@st.cache_resource
def get_chroma_instance():
  # Get the documents split into chunks
  docs = load_documents(rag_directory)

  # create the open-source embedding function
  embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

  # load it into Chroma
  return Chroma.from_documents(docs, embedding_function)

db = get_chroma_instance()


def query_documents(question):
  """
  Uses RAG to query documents for information to answer a question

  Example call:

  query_documents("What are the action items from the meeting on the 20th?")
  Args:
      question (str): The question the user asked that might be answerable from the searchable documents
  Returns:
      str: The list of texts (and their sources) that matched with the question the closest using RAG
  """
  similar_docs = db.similarity_search(question, k=5)
  docs_formatted = list(map(lambda doc: f"Source: {doc.metadata.get('source', 'NA')}\nContent: {doc.page_content}", similar_docs))

  return docs_formatted


def main():
  st.title("Chat with Local Documents")

if __name__ == "__main__":
  main()