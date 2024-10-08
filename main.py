import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import config
from src.routes import users

app = FastAPI()

app.include_router(users.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=config.PORT,
        host=config.HOST,
        reload=config.RELOAD,
        log_level="info",
    )