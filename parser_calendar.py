import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_event(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all script tags with type="application/ld+json"
        ld_json_scripts = soup.find_all('script', type='application/ld+json')
        
        # Iterate over each script tag
        for script in ld_json_scripts:
            print("Script content:", script.get_text())
    else:
        print("Failed to fetch page:", url)


def parse_page(url,unique_urls):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        div_content = soup.findAll('div', class_='item event_item vevent')

        for div in div_content:

            if div:
            # Find all <a> tags within the div
                links = div.find_all('a', href=True)
            
            # Iterate over each <a> tag
                for link in links:
                    href = link['href']
                
                # Filter URLs based on certain conditions
                    if 'https://calendar.colorado.edu/event' in href:
                        unique_urls.add(href)
     
    else:
        print("Failed to fetch page:", url)

start_url = "https://calendar.colorado.edu/calendar"


unique_urls = set()
parse_page(start_url, unique_urls)


parse_event("https://calendar.colorado.edu/event/international_coffee_hour_1555")

print("Unique URLs:")
# for url in unique_urls:
#     print(url)