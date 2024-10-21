import pandas as pd
from sqlalchemy import create_engine
from langchain_core.documents import Document
from langchain.document_loaders import UnstructuredURLLoader

def convert_data():
    engine = create_engine('mysql+pymysql://admin:awais@127.0.0.1:3307/plants')
    query = "SELECT * FROM plants.base_product;"
    product_data = pd.read_sql(query, engine)

    data = product_data[["name", "price", 'description', 'quantity', 'product_type_id', 'seller_id']]
    product_list = []

    for index, row in data.iterrows():
        obj = {
            'name': row['name'],
            'price': row['price'],
            'description': row['description'],
            'quantity': row['quantity'],
        }
        product_list.append(obj)

    docs = []
    for entry in product_list:
        page_content = f"Name: {entry['name']}\nPrice: {entry['price']}\nDescription: {entry['description']}\nQuantity: {entry['quantity']}"
        metadata = {"product_type_id": row['product_type_id'], "seller_id": row['seller_id']}
        doc = Document(page_content=page_content, metadata=metadata)
        docs.append(doc)
        
    urls = [
        # 'https://en.wikipedia.org/wiki/Python_(programming_language)',
        # 'https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d',
        # 'https://www.geeksforgeeks.org/web-development/?ref=home-articlecards',
        'https://awaisshakeel12.pythonanywhere.com/',
        'http://127.0.0.1:8000/',
        'http://127.0.0.1:8000/blog',
        'http://127.0.0.1:8000/community',
        'http://127.0.0.1:8000/adminpanel'
        
    ]    
    
    loader = UnstructuredURLLoader(urls=urls)
    data= loader.load()
    
    
    
    commbine = docs + data

    return commbine
