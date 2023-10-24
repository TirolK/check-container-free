from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def index():
 
    url = "https://www.homes.co.jp/trunkroom/b-12663/"
    
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, "html.parser")

    text = bs.find_all('td', {'class': 'btn'})

    return text