from fastapi import  status, APIRouter
from ..ai_script.chain import chain_conversation
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage
from ..ai_script.prompts import general_search_prompt
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Optional, Dict
from langchain.schema import HumanMessage, AIMessage
from bs4 import BeautifulSoup

router = APIRouter(
    prefix="/conversation",
    tags=['Conversation']  
)
    
# memory = ConversationBufferMemory(k=100,memory_key="chat_history", input_key="query", return_messages=True)

class MessageItem(BaseModel):
    content: str
    type: str
    
class DataModel(BaseModel):
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
         

@router.post("/chat/", status_code=status.HTTP_200_OK)
async def conversation(response: DataModel):
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
            general_search_prompt(response.data),
            memory
        )

        # Invoke chain
        result = chain.invoke({"query": response.data})      
        
        title = extract_title_from_response(result.get("text", ""))


        # Prepare memory for serialization
        serialized_history = [
            {
                "content": msg.content,
                "type": "human" if isinstance(msg, HumanMessage) else "ai"
            }
            for msg in memory.chat_memory.messages
        ]

        # Construct response
        json_result = {
            "query": result["query"],
            "title": title,  
            "chat_history": serialized_history,
            "memory": {
                "chat_history": serialized_history
            }
        }

        if "text" in result:
            json_result["text"] = result["text"]

        return json_result

    except Exception as e:
        return HTMLResponse(
            content=f"<html><body><h1>Error</h1><p>{str(e)}</p></body></html>",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        


def extract_title_from_response(response_text: str) -> str:
    try:
        soup = BeautifulSoup(response_text, 'html.parser')
        title_element = soup.find('title')
        if title_element and title_element.text.strip():
            return title_element.text.strip()
    except:
        pass
    return "Untitled Chat"  # Default title if nothing is found

