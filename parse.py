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

def get_sitemap_urls(xml):
    """Return the number of URLs in a website XML sitemap file"""
    
    supra = requests.get(xml)
    paran = BeautifulSoup(supra.content, "xml")

    urls_from_xml = []

    loc_tags = paran.find_all('loc')

    for loc in loc_tags:
        urls_from_xml.append(loc.get_text()) 
   
    return urls_from_xml
    
    
    for i in screen:
        r = requests.get (i, stream=True)
        g = gzip.GzipFile(fileobj=BytesIO(r.content))
        file = g.read()
    
