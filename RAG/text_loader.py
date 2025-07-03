# Document loaders -> Text splitters -> Vector Database -> Retrivers
# Document Loaders (many types) -> most used -> text Loader, pdf loader, Web Base Loader, CSV Loader
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

loader = TextLoader(file_path='./readme.txt',encoding='utf-8')
docs = loader.load()
#print(type(docs[0])) <class 'langchain_core.documents.base.Document'>
#print(type(docs)) <class 'list'>
# print(docs[0].page_content)
# print(docs[0].metadata)

template = PromptTemplate(template="Write a short summary for the topic:{topic}",input_variables=['topic'])

chain = template | model | parser
result = chain.invoke({'topic':docs[0].page_content})
print(result)