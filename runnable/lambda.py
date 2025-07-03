# Generate a joke -> 1. Runnable pass through to give the joke 2.Create a python function: to count the words in the text-> wrap it to create runnable

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model= ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

def word_len(text):
    return len(text.split())


#To generate a joke on a topic
template1 = PromptTemplate(template="Generate a funny joke on {topic}",input_variables=['topic'])
joke_chain = RunnableSequence(template1,model,parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_len)
})

chain = RunnableSequence(joke_chain,parallel_chain)
print(chain.invoke({'topic':'Cricket'}))