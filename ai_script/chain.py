from typing import Optional
from langchain.chains import LLMChain
from . import helpers
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from ..helpers.config import settings



def chain_prompt(prompt,data,length:int, model:Optional[str] = None):
    json_parser = JsonOutputParser()
    model = model.strip() if model and model.strip() else None

    if model is None:
        model = settings.groq_model_name
    chain = prompt | helpers.llm_function(length,model) | json_parser
    
    try:
        response = chain.invoke({"data": data})
        return response
    except Exception as e:
        print(f"Error in chain_prompt: {e}")
        raise
    
def quiz_chain_prompt(prompt, length: int, model: str):
    json_parser = JsonOutputParser()
    
    chain = prompt | helpers.llm_function(length, model) | json_parser
    
    try:
        # No `data` passed since the quiz doesn't need it
        response = chain.invoke({})
        return response
    except Exception as e:
        print(f"Error in chain_prompt: {e}")
        raise
    
    
  
def chain_conversation(model:str, prompt, memory):
  
    groq_chat = ChatGroq(
            groq_api_key=settings.groq_api_key, 
            model_name=model
    )
    chain = LLMChain(llm=groq_chat,prompt=prompt,memory=memory)


    # chain = prompt | groq_chat | memory

    return chain

def chain_quick_prompt(model:str, prompt ):
  
    groq_chat = ChatGroq(
            groq_api_key=settings.groq_api_key, 
            model_name=model
    )


    chain = prompt | groq_chat 

    return chain
