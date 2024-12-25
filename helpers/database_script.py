import sqlite3  
import json
from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from datetime import datetime


DB_PATH = "memory.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            device_model TEXT NOT NULL,
            session_id TEXT NOT NULL,
            memory_data TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
    

import json

def save_memory(device_id: str, session_id: str,title:str, memory):
    # Extract chat history from memory
    chat_history = []
    for message in memory.chat_memory.messages:
        # Only include content and type
        chat_history.append({
            "content": message.content,
            "type": getattr(message, "type", "human") 
        })

    # Convert chat history to JSON
    memory_data_json = json.dumps(chat_history)
    current_timestamp = datetime.now().isoformat()

    # Save to database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO conversation_sessions (device_model, session_id, memory_data,timestamp,title)
        VALUES (?, ?, ?, ?, ?)
    """, (device_id, session_id, memory_data_json,current_timestamp,title))
    conn.commit()
    conn.close()


def load_memory(device_id: str, session_id: str):
    # Create an empty memory object
    memory = ConversationBufferMemory(return_messages=True)

    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT memory_data FROM conversation_sessions
        WHERE device_model = ? AND session_id = ?
    """, (device_id, session_id))
    row = cursor.fetchone()
    conn.close()

    if row:
        # Deserialize memory_data
        memory_data = json.loads(row[0])
        for message in memory_data:
            if message["type"] == "human":
                memory.chat_memory.add_user_message(message["content"])
            elif message["type"] == "ai":
                memory.chat_memory.add_ai_message(message["content"])
    return memory

