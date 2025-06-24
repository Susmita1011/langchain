from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")
documents = ["Virat Kohli is an Indian criketer know for his aggressive batting and leadership.",
"MS Dhoni is an Indian professional cricketer who plays as a right-handed batter and a wicket-keeper.",
"Jasprit Jasbirsingh Bumrah is an Indian cricketer who plays for the India national team in all formats of the game and has captained India in Tests and T20Is. A right-arm fast bowler, Bumrah plays for Gujarat in domestic cricket and for Mumbai Indians in the Indian Premier League.",
"Sachin Ramesh Tendulkar is an Indian former international cricketer who captained the Indian national team."]
query = "Tell me about Mahendra Singh Dhoni"
# Convert the Documents available and the user query to embeddings
doc_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

#Cosine similarity search. Passing 2D list to the cosine similarity
score = cosine_similarity([query_embeddings],doc_embeddings)[0]

# Adding index value to the scores to get the highest one
index, score= sorted(list(enumerate(score)),key= lambda x:x[1])[-1]

print(query)
print("Result:",documents[index])
print("Similarity Score: ",score)