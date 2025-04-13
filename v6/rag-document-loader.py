from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

rag_directory = os.getenv('DIRECTORY', 'meeting_notes')


def load_documents(directory):
    # Load the PDF or txt documents from the directory
    loader = DirectoryLoader(directory)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    return docs

if __name__ == "__main__":
    main()