from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates

import requests
from bs4 import BeautifulSoup

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()

templates = Jinja2Templates(directory="templates")

@app.get("/", status_code=200)
def index(request: Request) -> dict:

    site_dic = {
        "ハローストレージ浜尻町": {
          "url": "https://www.homes.co.jp/trunkroom/b-12661/",
        },
        "ハローストレージ貝沢町": {
          "url": "https://www.homes.co.jp/trunkroom/b-12663/",
        },
        "ハローストレージ倉賀野町2": {
          "url": "https://www.homes.co.jp/trunkroom/b-12667/",
        },
        "ハローストレージ東貝沢町": {
          "url": "https://www.homes.co.jp/trunkroom/b-12668/",
        },
    }

    for name, value in site_dic.items():
        response = requests.get(value["url"])
        response.encoding = response.apparent_encoding
        bs = BeautifulSoup(response.text, "html.parser")

        site_dic[name]["price"] = bs.find_all('td', {'class': 'fee'})[-1].get_text()
        site_dic[name]["size"] = bs.find_all('td', {'class': 'breadth'})[-1].get_text()
        text = bs.find_all('td', {'class': 'btn'})[-1].get_text()
        site_dic[name]["result"] = "満室" if "満室のため、お問合せできません" in text else "空室"        

    return templates.TemplateResponse(
        "index.html", 
        {"sites": site_dic,"request": request}
    )