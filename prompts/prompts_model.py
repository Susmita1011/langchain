from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Defining the drop down menu for user
paper_title = st.selectbox("Select the Research Paper",["Invariant Subspace Decomposition","Attention is All you need","Causal Effect of Functional Treatment"])
style_input = st.selectbox("Select the Explaination Style",["Begineer Friendly","Intermediate","Mathematical Heavy"])
length_input = st.selectbox("Select the Length",["short(1-2 paragraphs)","medium length(3-5 paragraphs)","lengthy"])

#Load the template
template = load_prompt(path='template.json')

#filling the placeholders
prompt = template.invoke({
    'paper_title':paper_title,
    'style_input': style_input,
    'length_input': length_input
})

# Creating Streamlit simple App
st.header("Research Paper Summarizer")
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)