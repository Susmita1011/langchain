## Result.content ---> StrOutputParser LLM will directly return the response in string 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Model Definition
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#1st prompt --> Generate detailed report
template1 = PromptTemplate(template= """Write a detailed report on '{topic}'""",
                          input_variables=['topic'])


#2nd prompt --> Generate 5 line summary of the report
template2 = PromptTemplate(template= """Write a 5 line summary on the following text: '{text}'""",
                           input_variables=['text'])

topic = input("Enter a Topic to get summary: ")

#Creating a StrOutputParsers
parser = StrOutputParser()

#Forming a Chain Pipeline
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':topic})
print(result)