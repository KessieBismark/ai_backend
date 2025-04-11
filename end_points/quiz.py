from fastapi import status, APIRouter
from pydantic import BaseModel, ValidationError
from ..ai_script.prompts import german_quiz_prompt
from ..ai_script.chain import chain_prompt
from langchain_core.output_parsers import JsonOutputParser
from typing import List, Optional, Union


router = APIRouter(
    prefix="/quiz",
    tags=['quiz']  
)

class QuizQuestion(BaseModel):
    question: str  
    options: List[str]  
    correct_answer: Union[str, List[str]]  
    english_translation: str
    english_explanation: str 

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]  # A list of quiz questions

class DataModel(BaseModel):
    model:Optional[str] =None
    level:str
    

   
@router.post("/quiz/", status_code=status.HTTP_200_OK )
async def quiz_prompt_api(response:DataModel, max_retries: int = 4):
  
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        try:
            result = chain_prompt(german_quiz_prompt(response.level),response.level,8192, response.model.strip() )

            validated_result = QuizResponse(**result) 
            
            return validated_result.questions

        except ValidationError as val_error:
           continue
       
        except Exception as e:
            print(f"Error on attempt {attempt}: {e}")