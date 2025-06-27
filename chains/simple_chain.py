from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parsers = StrOutputParser()
template = PromptTemplate(template="Generate 5 interesting fact about the {topic}",
                          input_variables=["topic"])

topic = input("Enter a topic: ")
chain = template | model | parsers
result = chain.invoke({'topic': topic})
print(result)

# To see the chain flow: pip install grandalf
chain.get_graph().print_ascii()