from fastapi import  status, HTTPException, APIRouter
from pydantic import BaseModel, ValidationError
from typing import List
from ..ai_script.prompts import conversation_prompt,conversation_continuation_prompt
from ..ai_script.chain import chain_prompt
from typing import Optional, Dict
from langchain.schema import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from ..ai_script.chain import chain_conversation

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
    
class DataModel(BaseModel):
    data:str
    model:Optional[str] =None

@router.post("/interview/", status_code=status.HTTP_200_OK)
async def conversation_prompt_api(response:DataModel, max_retries: int = 4):
    attempt = 0

    while attempt < max_retries:
        attempt += 1
        try:

            result = chain_prompt(conversation_prompt,response. data, 8192,response. model.strip())
            
            try:
                validated_result = ConversationResponse(**result)
                return validated_result
            except ValidationError as val_error:
                # raise HTTPException(
                #     status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                #     detail=str(val_error)
                # )
                continue
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Error processing verb: {str(e)}"
            )
            
            
class MessageItem(BaseModel):
    content: str
    type: str
    
class ConvoModel(BaseModel):
    data:str
    model:str
    chat_memory: Optional[dict] = None

def create_memory_from_dict(chat_memory: Dict) -> ConversationBufferMemory:
    memory = ConversationBufferMemory(
        k=100,
        memory_key="chat_history",
        input_key="query",
        return_messages=True
    )
    
    if chat_memory and "chat_history" in chat_memory:
        # Reconstruct messages from the saved chat history
        messages = []
        for msg in chat_memory["chat_history"]:
            if msg["type"] == "human":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["type"] == "ai":
                messages.append(AIMessage(content=msg["content"]))
        
        # Set the reconstructed messages to memory
        memory.chat_memory.messages = messages
    
    return memory
         
         
@router.post("/interview-continuation/", status_code=status.HTTP_200_OK)
async def conversation_prompt_api(response:ConvoModel, max_retries: int = 4):
    attempt = 0
    



    while attempt < max_retries:
        attempt += 1
        try:
              # Create or restore memory
            if not response.chat_memory:
                memory = ConversationBufferMemory(
                    k=100,
                    memory_key="chat_history",
                    input_key="query",
                    return_messages=True
                )
            else:
                memory = create_memory_from_dict(response.chat_memory)

               # Create chain with the memory
            chain = chain_conversation(
                response.model.strip(),
                conversation_continuation_prompt(response.data),
                memory
            )
            result = chain.invoke({"query": response.data})
            try:
                validated_result = ConversationResponse(**result)
                return validated_result
            except ValidationError as val_error:
                # raise HTTPException(
                #     status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                #     detail=str(val_error)
                # )
                continue
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Error processing verb: {str(e)}"
            )