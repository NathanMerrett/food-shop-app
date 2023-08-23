import requests
from bs4 import BeautifulSoup
import time


def get_urls_from_sitemap(sitemap_url):
    # Fetch the sitemap content
    response = requests.get(sitemap_url)
    response.raise_for_status()
    
    # Parse the sitemap XML
    soup = BeautifulSoup(response.content, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    
    return urls

def download_data_from_urls(urls, download_path, delay=2):
    for idx, url in enumerate(urls, start=1):
        response = requests.get(url)
        response.raise_for_status()
        
        # Construct a filename based on the URL or any other logic you prefer
        filename = f"data_{idx}.html"
        with open(download_path + filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {url} to {filename}")

        # Introduce a delay before the next request
        time.sleep(delay)

if __name__ == "__main__":
    sitemap_url = "https://www.tesco.com/groceries/sitemap/UK.en.pdp.sitemap.xml"  # replace with the actual sitemap URL
    download_path = "./downloads/"  # make sure this directory exists
    
    urls = get_urls_from_sitemap(sitemap_url)
    download_data_from_urls(urls, download_path)
