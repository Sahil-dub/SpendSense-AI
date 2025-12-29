from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, category, expense

app = FastAPI(title="AI Expense Tracker")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend is running"}
