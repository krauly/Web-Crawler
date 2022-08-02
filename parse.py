import requests
from bs4 import BeautifulSoup

def get_page(url):
    """Crawls a URL and returns the HTML raw code
    
    Returns
    
    Soup : A string of ordered HTML source code"""
    web_page = requests.get(url, headers={'User-agent': 'Mozilla'})
    try:
        requests.exceptions.Timeout()
    except Exception as e:
        raise SystemExit(e)
        
        
    try:
        requests.exceptions.TooManyRedirects()
    except Exception as ext:
        raise SystemExit(ext)

    try:
        web_page.raise_for_status()
    except Exception as error:
        print(f"There was a problem {error}")
    
    soup = BeautifulSoup(web_page.content, 'lxml')
    
    return soup
