from langchain.chains import LLMChain
from . import helpers
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from ..helpers.config import settings

def chain_prompt(prompt,data,length:int, model:str):
    json_parser = JsonOutputParser()
    
    chain = prompt | helpers.llm_function(length,model) | json_parser
    
    try:
        response = chain.invoke({"data": data})
        return response
    except Exception as e:
        print(f"Error in chain_prompt: {e}")
        raise
    

  
def chain_conversation(model:str, prompt, memory):
    # client = Groq()
    # completion = client.chat.completions.create(
    #     model=model,
    #     messages=data,
    #     temperature=1,
    #     max_tokens=length,
    #     top_p=1,
    #     stop=None,
    # )
    groq_chat = ChatGroq(
            groq_api_key=settings.groq_api_key, 
            model_name=model
    )
    chain = LLMChain(llm=groq_chat,prompt=prompt,memory=memory)
    # chain = prompt | groq_chat | memory

    return chain