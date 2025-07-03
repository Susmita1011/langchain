# It provides the same output as it input without processing it

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough, RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()
 # LLM1 -> generate joke | 1. Runablepassthrough to get the joke too 2. LLM2 -> explain the joke
template1 = PromptTemplate(template="Generate a funny joke about {topic}",input_variables=['topic'])
template2 = PromptTemplate(template="Explain briefly about joke -> {text}",input_variables=['text'])

joke_chain = RunnableSequence(template1,model,parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(template2,model,parser)
})
chain = RunnableSequence(joke_chain,parallel_chain)
result = chain.invoke({'topic':'Doremon'})
print(result)
