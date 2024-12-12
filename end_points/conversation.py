from fastapi import  status, HTTPException, APIRouter
from ..ai_script.chain import chain_conversation
from langchain.memory import ConversationBufferMemory
from ..ai_script.prompts import general_search_prompt

router = APIRouter(
    prefix="/conversation",
    tags=['Conversation']  
)
    
memory = ConversationBufferMemory(k=50,memory_key="chat_history", return_messages=True)

@router.get("/{data}", status_code=status.HTTP_200_OK)
async def conversation(data: str, model:str):
    try: 
        chain = chain_conversation(model.strip(), general_search_prompt(data), memory)
        
        result = chain.invoke({"query": data})
        json_result = {
            "query": result["query"],
            "chat_history": [
                    {
                        "content": item.content,
                        "type":item.type 
                    }
                    for item in result["chat_history"] if hasattr(item, 'content')  
                ],
          
        }

        if "text" in result:
            json_result["text"] = result["text"]

        return  json_result          
        
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error processing conversation: {str(e)}"
        )