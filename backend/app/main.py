from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI(title="AI Expense Tracker")

# For now, no models yet
@app.get("/")
def root():
    return {"message": "Backend is running"}
