# StructuredOutputParser -> takes the output of LLM and parse the content to JSON Objet based on predefined schema
from langchain.output_parsers import StructuredOutputParser,ResponseSchema #available in langchain.output_parser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Creating a schema for model to follow:
schema = [
     ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
     ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
     ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]

#Defining the parser:
parser = StructuredOutputParser.from_response_schemas(schema)

#Defining the template
template = PromptTemplate(template= "Brief 5 facts about '{topic}'\n{format_instructions}",
                          input_variables=['topic'],
                          partial_variables={'format_instructions':parser.get_format_instructions()})

chain = template | model | parser
result = chain.invoke({'topic':'Black Hole'})
print(result)

'''
Here the data schema can be defined but the drawback is we cant validate the data with StructuredOutput Parser.
So for data validation we can use Pydantic Output parser
'''


