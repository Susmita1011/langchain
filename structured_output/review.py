from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing_extensions import TypedDict, Annotated
from pydantic import BaseModel, Field

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# class Review(TypedDict):
#     summary: Annotated[str,"A concise summary of the review"]
#     sentiment: Annotated[str,"Sentiment Analysis of the rview i.e. Positive, Nuetral, Negative"]
#Creating Review Class
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in the list")
    name: str = Field(description="This is the reviewer name")
    summary: str = Field(description="A concise summary of the review")
    sentiment: str = Field(description="Sentiment Analysis of the rview i.e. Positive, Nuetral, Negative")

structured_model = model.with_structured_output(Review)

result = dict(structured_model.invoke("""The course is awesome with great teaching style.I really liked the whiteboard and pentab form of teaching.
Review by - Susmita"""))

print(result)