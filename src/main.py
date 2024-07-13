from scraper import fetch_page_content

if __name__ == "__main__":
    homePage = fetch_page_content("https://savvydefi.io/")
    print(homePage)