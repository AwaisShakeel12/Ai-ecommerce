import os
from langchain_core.documents import Document

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from google.oauth2 import service_account
from .data_convert2 import convert_data
from langchain_community.vectorstores import Chroma 

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = r""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

credentials = service_account.Credentials.from_service_account_file(GOOGLE_APPLICATION_CREDENTIALS)
genai.configure(api_key='')

# Set up embedding
embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

# Chroma setup
pr_directory = "chroma_db"
vstore = Chroma(embedding_function=embedding, persist_directory=pr_directory)

def ingest_documents():
    docs = convert_data()
    doc_ids = [f"doc_{i}" for i in range(len(docs))]
    inserted_ids = vstore.add_documents(docs, ids=doc_ids)
    vstore.persist()
    return vstore, inserted_ids
