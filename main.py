import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = [p.text for p in soup.find_all('h2')]
    return content

def scrape_all_urls():
    urls = [
        "https://www.noticiasagricolas.com.br/noticias/milho/",
        "https://www.noticiasagricolas.com.br/noticias/agronegocio/",
        "https://www.noticiasagricolas.com.br/noticias/cafe/",
        "https://www.noticiasagricolas.com.br/noticias/soja/"
    ]
    
    scraped_data = {}
    for url in urls:
        scraped_data[url] = scrape_website_content(url)
    
    with open('website_content.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    while True:
        scrape_all_urls()
        print("Scraping completed. Waiting for 5 minutes before next run.")
        time.sleep(300)  # Wait for 5 minutes
