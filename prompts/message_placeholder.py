## Important when the older chat is retrived from a file / Database
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate([('system','You are a helpful assistant'),
                               MessagesPlaceholder(variable_name='chat_history'),
                               ('human','{query}')])

#Defining chat history from the file
chat_history = []
with open('message.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

prompt = template.invoke({'chat_history': chat_history,'query':"Where is my refund?"})

print(prompt)