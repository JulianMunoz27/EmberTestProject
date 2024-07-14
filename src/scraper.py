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

#check all the documents to scrape
def scrape_all_docs():
    try:
        base_url = "https://docs.savvydefi.io/"
        soup = fetch_page_content(base_url)

        if not soup:
            print("Failed to fetch page content.")
            return []

        docs_links = []
        for a_tag in soup.find_all('a', class_=lambda x: x and 'flex flex-row justify-between pl-5' in x):
            href = a_tag.get('href')
            if href:
                if href.startswith('/'):
                    full_url = base_url.rstrip('/') + href
                elif not href.startswith('http'):
                    full_url = base_url.rstrip('/') + '/' + href
                else:
                    full_url = href
                docs_links.append(full_url)

        docs_data = []
        for doc_url in docs_links:
            doc_soup = fetch_page_content(doc_url)
            if doc_soup:
                doc_title = doc_soup.title.string if doc_soup.title else ""
                doc_data = {
                    "url": doc_url,
                    "title": doc_title,
                    #"content": doc_soup.get_text() #uncomment this if the content of the page is required
                }
                docs_data.append(doc_data)

            else:
                print("Failed to fetch content")

        return docs_data
    except Exception as error:
        print(error)

#get the results of the scraping text in home page and the documents section
def build_index():
    index = {
        "home_page": scrape_home_page(),
        "docs": scrape_all_docs()
    }
    return index