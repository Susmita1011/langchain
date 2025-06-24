from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Defining the messages

messages = [SystemMessage(content="You are an expert Cyber Security Architect"),HumanMessage(content="Help me Secure Azure VM in 5 bullet points with only heading")]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)