## Generate a report -> check for words in the report if > 500, then summarize the report again, else print it
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence,RunnableBranch,RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

template1 = PromptTemplate(template="Generate a detailed report on topic: {topic}",input_variables=['topic'])
template2 = PromptTemplate(template="Summarize the topic: {text}",input_variables=['text'])

report_chain = RunnableSequence(template1,model,parser)
branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(template2,model,parser)),
    #default or else
    RunnablePassthrough()
)
chain = RunnableSequence(report_chain,branch_chain)
result = chain.invoke({'topic':'Russia Vs Ukraine'})
print(result)