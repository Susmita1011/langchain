from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

def doc_loader(path):
    loader = TextLoader(file_path=path,encoding='utf-8')
    doc = loader.load()
    return doc[0].page_content

prompt = PromptTemplate(template="Summarize briefly in bullet points about the topic:{topic}",input_variables=['topic'])

runnable_func = RunnableLambda(doc_loader)

chain = runnable_func | prompt | model | parser
result = chain.invoke('./readme.txt')
print(result)