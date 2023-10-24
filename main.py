from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def index():
    return {
        name: "えみちゃん好き",
        date: datetime.datetime.today()
    }