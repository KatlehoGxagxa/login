"""
    Create environment: python -m venv env
    Activate environment: source ".\env\Scripts\activate"
    Update requirements.txt: pip freeze > requirements.txt
    Install requirements: pip install -r requirements.txt       #run command after every git pull
    run the program: uvicorn app.main:app --port 8000 --reload      or      hypercorn app.main:app --reload

"""

from fastapi import FastAPI

app = FastAPI()

from app.registration import route

app.include_router(route.router)

@app.get("/")
async def root():
    return "Scorpion King"
