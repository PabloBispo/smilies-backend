from typing import Optional, Dict

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping")
def ping_pong() -> Dict[str, str]:
    return {
        "ping": "pong"
    }
