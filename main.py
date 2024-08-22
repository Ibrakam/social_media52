from fastapi import FastAPI

from api.photo_api.photo import photo_router
from api.user_api.user import user_api
from api.post_api.post import post_router
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine

Base.metadata.create_all(engine)


app = FastAPI(docs_url="/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user_api)
app.include_router(post_router)
app.include_router(photo_router)
