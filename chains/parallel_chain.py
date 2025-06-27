#Big file with multiple texts -> Generate notes and generate quiz parallely ->LLM to merge both -> User Output
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

load_dotenv()

#Model Initiation
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Creating templat1 -> To create notes for the text
template1 = PromptTemplate(template="Create a simple notes from the following text \n {text}",input_variables=['text'])

#Creating template2 -> to create quiz from the text
template2 = PromptTemplate(template="Generate 5 short question answers from the following text \n {text}",input_variables=['text'])

#Create template3 -> To merege the outputs
template3 = PromptTemplate(template="Merge the following notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}",input_variables=['notes','quiz'])

#Initializing the String Parser
parser = StrOutputParser()

#Defining the chain for the parallel processing/chain we need RunnableParallel:
#RunnableParallel is runnable required to execute multiple parallel chains in langchain
#parallel_chain running parallely for both notes and quiz

parallel_chain = RunnableParallel({
    'notes': template1 | model | parser,
    'quiz': template2 |model |parser
})

#Merging the above results into single document
merge_chain = template3 | model | parser

#Final Chain
chain = parallel_chain | merge_chain

text = []
with open("langchain.txt",'r') as f:
    text.extend(f.readlines())

result = chain.invoke({'text':text})
print(result)
