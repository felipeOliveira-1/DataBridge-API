import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Exclui scripts e estilos do conteúdo
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Extrai o texto de todo o documento HTML
    text = soup.get_text()
    
    # Separa em linhas e remove espaços em branco no início e no fim de cada linha
    lines = (line.strip() for line in text.splitlines())
    # Quebra as linhas em segmentos para tratar múltiplos espaços e tabs
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Remove linhas em branco
    text_content = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text_content


def scrape_all_urls():
    urls = [
        "https://www.canalrural.com.br/agricultura/"
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
        print("Scraping completed. Waiting for 2 minutes before next run.")
        time.sleep(100)  # Wait for 2.5 minutes
