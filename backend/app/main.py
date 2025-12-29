from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, category, expense
from app.routers import auth

app = FastAPI(title="AI Expense Tracker")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Backend is running"}
