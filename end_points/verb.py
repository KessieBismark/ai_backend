from fastapi import status, HTTPException, APIRouter
from pydantic import BaseModel, ValidationError
from ..ai_script.prompts import verb_prompt
from ..ai_script.chain import chain_prompt


router = APIRouter(
    prefix="/verb",
    tags=['Verbs']  
)

class VerbResponse(BaseModel):
    german_data: str
    data_forms: dict
    example_sentences: dict

@router.post("/{verb}", status_code=status.HTTP_200_OK)
async def verb_prompt_api(verb: str,model:str):
    try:
        result = chain_prompt(verb_prompt, verb, 2024,model.strip())

        try:
            validated_result = VerbResponse(**result)
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
        