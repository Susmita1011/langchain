from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-exp-03-07')
embeddings = model.embed_query("New Delhi is Capital of India")
print(str(embeddings))