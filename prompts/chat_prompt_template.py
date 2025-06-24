from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

#Loading the key
load_dotenv()

#Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

agent = input("Enter the Domain: ")
topic = input("Enter the topic: ")
'''
template = ChatPromptTemplate([SystemMessage(content="You are a helpful {agent} assistant"),HumanMessage(content="Explain in simple terms about {topic}")])

Okay, I will explain {topic} in simple terms:
rather write the way below:

template = ChatPromptTemplate.from_messages([('system','You are a helpful {agent} assistant'),('human','Explain in simple terms about {topic}')])

Or
template = ChatPromptTemplate([('system','You are a helpful {agent} assistant'),('human','Explain in simple terms about {topic}')])
'''
template = ChatPromptTemplate.from_messages([('system','You are a helpful {agent} assistant'),('human','Explain in simple terms about {topic}')])

prompt = template.invoke({
    'agent':agent,
    'topic': topic
})

result = model.invoke(prompt)
print(result.content)