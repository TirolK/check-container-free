from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def index():
    return time.time()