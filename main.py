from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def index():
 
    url = "https://www.sejuku.net/blog/"
    
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    return response.text