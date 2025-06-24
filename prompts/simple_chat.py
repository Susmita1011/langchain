from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# while True:
#     user_input = input("User: ")
#     if user_input == 'exit':
#         break
#     else:
#         result = model.invoke(user_input)
#         print("AI: ",result.content)

# With this the AI doesnt know the previous chats as it dont have a context here. By default it doesnt have the access to older chats.
# To resolve this we need to maintain the chat history ourselves

# chat_history = []

# while True:
#     user_input = input("User: ")
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     else:
#         result = model.invoke(chat_history) #invoke can take single line or sequence as well
#         chat_history.append(result.content)
#         print("AI: ",result.content)
# print(chat_history)
'''
['Which is greater 2 or 0', '2 is greater than 0.', 'Multiple greater number by 10', "You didn't specify which number to multiply by 10. Since we established that 2 is greater than 0, I'll assume you want to multiply 2 by 10.\n\n2 * 10 = 20", 'Add the above result with 5', '20 + 5 = 25', 'Awesome!', "Great! I'm glad I could help. Is there anything else I can do for you?", 'exit']

It solves the above problem but still there is a issue. Each message shows the conversation but we cant really know who sent which message. When the chats grow for AI to answer properly it should knw what it has sent earlier and what user asked. 

So as a solution we use Messages
'''
message = [SystemMessage(content= 'You are a helpful assistant'),HumanMessage(content='')]

while True:
    user_input = input("User: ")
    message.append(HumanMessage(content=user_input))
    if user_input == "exit":
            break
    else:
        result = model.invoke(message)
        print("AI: ",result.content)
        message.append(AIMessage(content=result.content))
print(message)

