import requests
from bs4 import BeautifulSoup
import json
from utilities.hash import generate_hash
from dynamo.dynamo_db_format import convert_to_dynamodb_format

def parse_event(url):

    response = requests.get(url)

    if response.status_code == 200:

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all script tags with type="application/ld+json"
        ld_json_scripts = soup.find_all('script', type='application/ld+json')
        data = json.loads(ld_json_scripts[0].get_text())
        json_data = {}

        for index_json in data:

            try:
                json_data['title'] = index_json['name']
                json_data['description'] = index_json['description']
                json_data['startDate'] = index_json['startDate']
                json_data['endDate'] = index_json['endDate']
                json_data['eventStatus'] = index_json['eventStatus']
                #json_data['location'] = index_json['location']
                json_data['url'] = index_json['url']
                json_data['image'] = index_json['image']

                id = json_data['url'] + json_data['startDate']
                hash_id = generate_hash(id)
                json_data['hash_id'] = hash_id

                json_data = convert_to_dynamodb_format(json_data)

                return json_data
            
            except:
                pass

    else:
        print("Failed to fetch page:", url)
