"""
    Create environment: python -m venv env
    Activate environment: source ".\env\Scripts\activate"
    Update requirements.txt: pip freeze > requirements.txt
    Install requirements: pip install -r requirements.txt       #run command after every git pull
    run the program: uvicorn app.main:app --reload      or      hypercorn app.main:app --reload

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Scorpion King"
