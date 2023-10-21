from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.quiz.api import quiz_router





app = FastAPI(
    title="Bewise-test"
)


origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type",
                   "Set-Cookie",
                   "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)


app.include_router(quiz_router)