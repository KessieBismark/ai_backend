from fastapi import  status, HTTPException, APIRouter
from groq import Groq
from helpers.config import settings



router = APIRouter(
    prefix="/model",
    tags=['Model']  
)


@router.get("/model-list/", status_code=status.HTTP_200_OK)
async def ai_models():
    try:
        client = Groq(
            api_key=settings.groq_api_key,
        )

        models = client.models.list()

        print(models)
        return models

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error processing verb: {str(e)}"
        )