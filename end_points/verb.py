from fastapi import status, APIRouter
from pydantic import BaseModel, ValidationError
from ..ai_script.prompts import verb_prompt
from ..ai_script.chain import chain_prompt
from langchain_core.output_parsers import JsonOutputParser


router = APIRouter(
    prefix="/verb",
    tags=['Verbs']  
)

class VerbResponse(BaseModel):
    german_data: str
    data_forms: dict
    example_sentences: dict



class DataModel(BaseModel):
    verb:str
    model:str
    

   
@router.post("/verb_query/", status_code=status.HTTP_200_OK )
async def verb_prompt_api(response:DataModel, max_retries: int = 4):
  
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        try:
            result = chain_prompt(verb_prompt, response.verb, 2024, response.model.strip())
            validated_result = VerbResponse(**result) 
            return validated_result

        except ValidationError as val_error:
           continue
       
        except Exception as e:
            print(f"Error on attempt {attempt}: {e}")