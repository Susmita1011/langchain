# User prompt -> LLM summarizes -> LLM then drafts 5 pointers -> Output to User
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

#Load the credential:
load_dotenv()

#Model definition
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

topic = input("Enter a topic to summarize: ")

#Template-1
template1 = PromptTemplate(template="Give me a brief summary on {topic}",input_variables=['topic'])

#Template - 2
template2 = PromptTemplate(template="Give me main points from {text} in 5 lines",input_variables=['text'])

#Initializing the parser
parsers = StrOutputParser()

chain = template1 | model | parsers | template2 | model | parsers
result = chain.invoke({'topic':topic})
print(result)