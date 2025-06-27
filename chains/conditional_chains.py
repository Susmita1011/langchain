# Review -> LLM to analyze the sentiment -> If positive the LLM to generate positive respose -> If negative then LLM to generate a response accordingly

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from typing_extensions import Literal
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda

load_dotenv()
#Initializing the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Fixing the response
class analysis(BaseModel):
    sentiment: Literal['Positive','Nuetral','Negative'] = Field(description="Give the sentiment of the feedback")

#Initilaizing the Pydantic Parser:
parser = PydanticOutputParser(pydantic_object=analysis)
parser1 = StrOutputParser()

#Template-1
template1 = PromptTemplate(template="Classify the {review} based on the sentiment \n {format_instruction}",input_variables=['review'],partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template1 | model | parser
#result = chain.invoke({'review':"I dont see any fault but dnt see any good thing as well"}).sentiment
# print(result)

# To do conditional chain execution, RunnableBranch is used from the langchain.schema.runnable like Runableparrallel used for the parrallel chain execution
'''
branch_chain = RunnableBranch((condition,which chain to execute if condition true),(condition2,chain2),default chain(if nothing is true then this executes))
'''
#Template for Positive Block
template_true = PromptTemplate(template="Generate a generic and appropriate response of maximum 2 lines for a positive feedback \n feedback -> {feedback}",input_variables=['feedback'])

#Template for Negative Block
template_neg = PromptTemplate(template="Generate a generic and appropriate response of maximum 2 lines for the a negative feedback \n feeback -> {feedback}",input_variables=['feedback'])

#Template for Nuetral Block
template_neutral = PromptTemplate(template="Generate a generic and appropriate response of maximum 2 lines for a nuetral feedback \n feeback -> {feedback}",input_variables=['feedback'])

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive',template_true | model | parser1),
    (lambda x:x.sentiment == 'Negative',template_neg | model | parser1),
    (lambda x:x.sentiment == 'Nuetral',template_neutral | model | parser1),
    RunnableLambda(lambda x: "Could not evaluate the sentiment")
)

# Chain for the analysis , branch_chain for condition

merge_chain = chain | branch_chain
result = merge_chain.invoke({'review':"This is a terrible Phone"})
print(result)
merge_chain.get_graph().print_ascii()