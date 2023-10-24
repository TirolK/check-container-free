from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def index():
    return datetime.datetime.today()