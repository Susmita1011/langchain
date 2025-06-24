from langchain_core.prompts import PromptTemplate



#Defining the template with user variable
template = PromptTemplate(template = """Please summarize the research paper titled "{paper_title}" with the following specifications:
Explaination style: {style_input}
Explannation length: {length_input}
1. Mathematical Details:
  - Include relevant mathematical equations if present in the paper
  - Explain the mathematical concept in simple, intutitve code snippet where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in paper . respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate and alligned with provided style and length
""",
input_variables=['paper_title','style_input','length_input'],
validate_template=True #checkes if the all the input mentioned in template is available with input_variables. If not then it will generate error
)


#Saving the template for later use
template.save('template.json')