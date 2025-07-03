# RunnableParallel Exceutes parallely generating output in dictionary
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

template1 = PromptTemplate(template="Generate a brief Tweet on the topic: {topic}",input_variables=['topic'])
template2= PromptTemplate(template="Generate a brief LinkedIn post on the topic:{topic}",input_variables=['topic'])

chain = RunnableParallel({
    'tweet': RunnableSequence(template1 | model | parser),
    'linkedIn': RunnableSequence(template2 | model | parser)
})

result = chain.invoke({'topic':'Global Warming'})

print(result['linkedIn'])
print(result['tweet'])