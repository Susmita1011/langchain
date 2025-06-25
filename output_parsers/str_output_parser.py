## Result.content ---> StrOutputParser LLM will directly return the response in string 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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
#prompt1 = template1.invoke({'topic':topic})
#result = model.invoke(prompt1)
#prompt2 = template2.invoke({'text':result.content})
#result = model.invoke(prompt2)
#print(result.content)

chain = template1 | model
chain1 = template2 | model
intermediate_res = chain.invoke({'topic':topic})
result = chain1.invoke({'text':intermediate_res.content})
print(result.content)