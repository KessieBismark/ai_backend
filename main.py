from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .end_points import prompt_conversation, verb,list_model,conversation

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(verb.router)
app.include_router(prompt_conversation.router)
app.include_router(list_model.router)
app.include_router(conversation.router)



# "llama3-8b-8192"