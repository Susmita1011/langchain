## generate a joke from a llm and then pass it to other llm to express it and reflect the final output
from langchain.schema.runnable import RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

#Defining the 1st template
template1 = PromptTemplate(template="Generate a funny joke based on a {topic}",input_variables=['topic'])

topic = input("Enter a topic: ")

template2 = PromptTemplate(template="Explain the {text} in details to the user ",input_variables=['text'])

chain = RunnableSequence(template1,model,parser,template2,model,parser)

result = chain.invoke({'topic':topic})
print(result)