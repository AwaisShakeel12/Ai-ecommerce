from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from .ingest2 import ingest_documents
from langchain_groq import ChatGroq

# Ingest documents and set up the retriever
vstore, _ = ingest_documents()
retriever = vstore.as_retriever(search_kwargs={"k": 3})

# Prompt and LLM chain setup
PRODUCT_BOT_TEMPLATE = """
Your e-commerce bot is an expert in product recommendations and customer queries.
It analyzes product titles and reviews to provide accurate and helpful responses.
Provide users information about the this e-commerce store. ask them for there choice according to context if user 
ask suggestion from you. try to sale product by encourage them. 
Ensure your answers are relevant to the product context and refrain from straying off-topic.
Your responses should be concise and informative.

CONTEXT:
{context}

QUESTION: {question}

YOUR ANSWER:
"""

prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

llm = ChatGroq(model='llama-3.1-70b-versatile', groq_api_key='')

# Build the chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
