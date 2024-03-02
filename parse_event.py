import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

def parse_event(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all script tags with type="application/ld+json"
        ld_json_scripts = soup.find_all('script', type='application/ld+json')
        
        # Iterate over each script tag
        for script in ld_json_scripts:
            # print("Script content:", script.get_text())
            data = json.loads(script.get_text())
            for index_json in data:
                print(index_json['name'])
                print(index_json['description'])
                print(index_json['startDate'])
                print(index_json['endDate'])
                print(index_json['eventStatus'])
                print(index_json['location'])
                print(index_json['url'])
                print(index_json['image'])


    else:
        print("Failed to fetch page:", url)
