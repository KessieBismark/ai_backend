from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    groq_api_key: str = Field(
        default=None,  # Allow None as a default
        alias="GROQ_API_KEY"
    )
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }
    
    groq_model_name: str = "llama3-70b-8192"  # Default model name
    def __init__(self, **data):
        # Explicitly get the environment variable
        env_api_key = os.getenv('GROQ_API_KEY')
        
        # If the environment variable is not found, raise a more informative error
        if not env_api_key:
            raise ValueError("GROQ_API_KEY must be set in the environment or .env file")
        
        # Call the parent constructor
        super().__init__(**data)

# Create settings instance
settings = Settings()

# Verify the API key is loaded
print(f"API Key loaded: {bool(settings.groq_api_key)}")