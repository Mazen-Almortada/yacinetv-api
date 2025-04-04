from fastapi import Header, HTTPException, Depends
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

def verify_token(Token: str = Header(...)):
    if Token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
