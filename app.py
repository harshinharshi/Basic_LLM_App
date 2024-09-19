from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Langsmith Tracking
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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" # add your langchain API key
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="Basic gemma2:2b app" # add your langchain project name

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a veterinarian, anwer only the questions related to animals and their health"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("veterinarian bot using Gemma Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


