from fastapi import FastAPI
from models import create_db_and_tables

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/db")
async def db():
    success = create_db_and_tables()
    if success:
        return {"message": "Hero table created"}
    else:
        return {"message": "No database connected"}
