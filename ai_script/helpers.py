from langchain_groq import ChatGroq
from helpers.config import settings



def llm_function(length:int, model:str):
    llm = ChatGroq(groq_api_key=settings.groq_api_key,  model=model,temperature=1,
         max_tokens=length,
        stop=None,)
    return llm


