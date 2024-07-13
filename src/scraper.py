import requests
from bs4 import BeautifulSoup

#This 
def fetch_page_content(url):
    response = requests.get(url)
    status = response.raise_for_status()
    result = ""

    if status == None:
        result = BeautifulSoup(response.text, 'html.parser')
    else:
        result = status
    
    return result
