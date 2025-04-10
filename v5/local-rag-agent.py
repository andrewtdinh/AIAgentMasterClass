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

def main():
  st.title("Chat with Local Documents")

if __name__ == "__main__":
  main()