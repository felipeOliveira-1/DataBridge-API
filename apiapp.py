from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI(title="DataBridge API")

class ContentItem(BaseModel):
    url: str
    content: list

class WebsiteContent(BaseModel):
    data: list[ContentItem]

def load_json_data():
    with open('website_content.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return WebsiteContent(data=[ContentItem(url=k, content=v) for k, v in data.items()])

@app.get("/data", summary="Fetches scraped data from the JSON file", response_model=WebsiteContent)
def get_scraped_data():
    return load_json_data()
