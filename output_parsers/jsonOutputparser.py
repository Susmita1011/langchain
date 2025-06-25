# Forces LLM to send output in JSON fromat
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = JsonOutputParser()

template = PromptTemplate(template=""" Give me name, age,city of a fictional person \n {format_instruction}""",
                                  input_variables=[],partial_variables={'format_instruction': parser.get_format_instructions()})

chain = template | model | parser  # directly parse the model Output 
result = chain.invoke({})
print(result)

# prompt = template.format()
# result = model.invoke(prompt)
# final_res = parser.parse(result.content)  # Convert JSOn string to JSON/Dict format
# print(final_res)

"""
Here we dnt decide the schema but the LLM do. which is not ideal for many cases. To enforce a schema to LLM response JSONOutputParser is not ideal. For that StructureOutputParser comes to picture

"""