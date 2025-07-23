from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()


model=ChatGroq(model="Gemma2-9b-It")

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser=StrOutputParser()

##create chain
chain=prompt_template|model|parser

# App Defination
app=FastAPI(
    title="Langchain Groq Server",
    description="A simple Langchain Groq server",
    version="0.1.0"
)

# adding chain routes

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)