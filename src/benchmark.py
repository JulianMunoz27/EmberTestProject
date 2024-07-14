import time
import json
import os
import requests

from bs4 import BeautifulSoup
from scraper import build_index, scrape_all_docs

#benchmark how much it takes to fetch the home page
def benchmark_discovery_protocol_query():
    start_time = time.time()
    requests.get("https://savvydefi.io/")
    end_time = time.time()
    print("Discovery Protocol Query Time: {:.2f} ms".format((end_time - start_time) * 1000))

#benchmark how much it takes to get the text from the homepage
def benchmark_retrieving_embeddings():
    start_time = time.time()
    url = "https://savvydefi.io/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    home_page_data = {
            "title": soup.title.string if soup.title else "",
            "content": soup.get_text()
    }

    end_time = time.time()
    print("Retrieving Embeddings Time: {:.2f} ms".format((end_time - start_time) * 1000))

#saves the documents into json files
def save_documents_to_json(samples, directory, prefix):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i, sample in enumerate(samples):
        file_path = os.path.join(directory, "{}_{}.json".format(prefix, i+1))
        with open(file_path, 'w') as f:
            json.dump(sample, f, indent=4)

#takes a certain amount of documents from the scrape and send them to be saved
def save_scraped_documents(index):
    items = index['docs'][:10]
    save_documents_to_json(items, "documents", "document")

def main():
    index = build_index()
    benchmark_discovery_protocol_query()
    benchmark_retrieving_embeddings()
    save_scraped_documents(index)

if __name__ == "__main__":
    main()