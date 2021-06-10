from fastapi import FastAPI
from app.registration import route

"""
    Run the app: uvicorn app.registration.main:app --port 8001 --reload
    
"""

app = FastAPI()

app.include_router(route.router)

@app.get("/")
async def root():
    return "Scorpion King"
