from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.connection import conn
from routes.calc import calc_router
import uvicorn

app = FastAPI()

app.include_router(calc_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

@app.on_event("startup")
def on_startup():
    conn()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
