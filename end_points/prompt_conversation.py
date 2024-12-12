from fastapi import  status, HTTPException, APIRouter
from pydantic import BaseModel, ValidationError
from typing import List
from ..ai_script.prompts import conversation_prompt
from ..ai_script.chain import chain_prompt

router = APIRouter(
    prefix="/prompt_conversation",
    tags=['Prompt Conversation']  
)

class ConversationLine(BaseModel):
    speaker: str
    german: str
    english: str

class ConversationResponse(BaseModel):
    conversation: List[ConversationLine]

@router.post("/{data}", status_code=status.HTTP_200_OK)
async def conversation_prompt_api(data: str, model:str):
    try:

        result = chain_prompt(conversation_prompt, data, 8192,model.strip())
        
        try:
            validated_result = ConversationResponse(**result)
            return validated_result
        except ValidationError as val_error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(val_error)
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error processing verb: {str(e)}"
        )