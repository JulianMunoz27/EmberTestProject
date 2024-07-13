import requests
from bs4 import BeautifulSoup

#This do the request to the url and the raise_for_status function returns if there're error or no and returns the content of the url in case the url is accessible
def fetch_page_content(url):
    try:
        response = requests.get(url)
        status = response.raise_for_status()
        result = ""

        if status == None:
            result = BeautifulSoup(response.text, 'html.parser')
        else:
            result = status
        
        return result
    except Exception as error:
        print(error)    
