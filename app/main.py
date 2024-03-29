from fastapi import FastAPI
from routers import messages

app = FastAPI()

app.include_router(messages.router)
