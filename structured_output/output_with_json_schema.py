from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from langchain_google_genai.llms import GoogleGenerativeAI
from dotenv import load_dotenv
from typing_extensions import TypedDict, Annotated
from pydantic import BaseModel, Field

load_dotenv()
model = ChatVertexAI(model="gemini-2.0-flash")
# Defining the Review schema:
## JSON Schema sample:

review_schema = {
  "title": "Review",
  "type": "object",
  "properties":{
     "key_themes":{
           "type": "array",
	 "items": {
	     "type": "string"
	     },
	    "description": "Write down all the key themes mentioned in review in list"
	     },
      "summary": {
          "type": "string",
	 "description": "A brief summary about the review provided"
	 },
      "sentiment":{
          "type": "string",
	"enum": ["positive","nuetral","negative"],
	"description":"Return the sentiment found in the review"
	},
      "name": {
         "type": ["string","null"],
          "description": "Write the name of the reviewer"
	}
	},
      "required": ["key_themes","summary","sentiment"]
      }

structured_model = model.with_structured_output(review_schema)

result = dict(structured_model.invoke("""The course is awesome with great teaching style.I really liked the whiteboard and pentab form of teaching.
Review by - Susmita"""))

print(result)