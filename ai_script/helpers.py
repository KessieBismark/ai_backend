from langchain_groq import ChatGroq
from ..helpers.config import settings
# from langchain_core.output_parsers import BaseOutputParser
import json



def llm_function(length:int, model:str):
    llm = ChatGroq(groq_api_key=settings.groq_api_key,  model=model,temperature=1,
         max_tokens=length,
        stop=None,)
    return llm


# class CustomJsonOutputParser(BaseOutputParser):
#     def parse(self, text: str):
#         try:
#             return json.loads(text)
#         except json.JSONDecodeError as e:
#             raise ValueError(f"Failed to parse JSON: {e}")