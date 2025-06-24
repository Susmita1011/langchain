from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

#Load the creedntials
load_dotenv()

#Defing the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.7)

#Loading the template
template = load_prompt(path='template.json')

#Streamlit UI
st.header("Research Paper Summarizer")
paper_title = st.selectbox("Select the Research Paper",["Invariant Subspace Decomposition","Attention is All you need","Causal Effect of Functional Treatment"])
style_input = st.selectbox("Select the Explaination Style",["Begineer Friendly","Intermediate","Mathematical Heavy"])
length_input = st.selectbox("Select the Length",["short(1-2 paragraphs)","medium length(3-5 paragraphs)","lengthy"])

if st.button("Summarize"):
    #Chain the action.-> Template invoke , model invoke (Earlier we first invoked template bu template.invoke = prompt and then later passed it to model.invoke)
    chain = template | model
    result = chain.invoke({
        'paper_title':paper_title,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result)
