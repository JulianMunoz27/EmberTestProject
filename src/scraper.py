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

#scrape the savvydefi home page
def scrape_home_page():
    try:
        url = "https://savvydefi.io/"
        soup = fetch_page_content(url)

        home_page_data = {
            "title": soup.title.string if soup.title else "",
            "content": soup.get_text()
        }

        return home_page_data
    except Exception as error:
        print(error)

#scrape the document from savvydefi
def scrape_docs_page(doc_url):
    try:
        soup = fetch_page_content(doc_url)

        doc_page_data = {
            "url": doc_url,
            "title": soup.title.string if soup.title else "",
            #uncomment in case the contents are required
            #"content": soup.get_text()
        }

        return doc_page_data
    except Exception as error:
        print(error)

#check all the documents to scrape
def scrape_all_docs():
    try:
        home_url = "https://savvydefi.io/"
        soup = fetch_page_content(home_url)

        docs_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if "docs" in href: 
                full_url = href if href.startswith("http") else home_url + href
                docs_links.append(full_url)
        
        docs_data = [scrape_docs_page(doc_url) for doc_url in docs_links]
        
        return docs_data
    except Exception as error:
        print(error)

#get the results of the scraping of the home page and the documents section
def build_index():
    index = {
        "home_page": scrape_home_page(),
        "docs": scrape_all_docs()
    }
    return index