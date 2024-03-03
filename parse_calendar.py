import sys
sys.path.insert(1, './parser/')

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from parse_event import parse_event

start_url = "https://calendar.colorado.edu/calendar"

def parse_page(url, unique_urls):
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

def get_json_data(unique_urls, data_list):

    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(parse_event, url) for url in unique_urls]

        # Wait for all tasks to complete (optional)
        for future in as_completed(futures):
            try:
                # Get the result of the task
                result = future.result()
                if result is not None:
                    data_list.append(result)
                # Process result here (if needed)
            except Exception as exc:
                print(f'Generated an exception: {exc}')

###

# unique_urls = set([
#     'https://calendar.colorado.edu/event/french_bavardages',
#     'https://calendar.colorado.edu/event/i_love_mondays_mar11',
#     'https://calendar.colorado.edu/event/cu_cafe_coffee_hour',
#     'https://calendar.colorado.edu/event/cmci_drop_in_advising_sp24',
#     'https://calendar.colorado.edu/event/envs_monthly_coffee_hour',
#     'https://calendar.colorado.edu/event/charreria_exploring_the_human-horse_connection_in_mexican_rodeo',
#     'https://calendar.colorado.edu/event/russian_tea_conversation_hour_4732',
#     'https://calendar.colorado.edu/event/russian_tea_conversation_table',
#     'https://calendar.colorado.edu/event/ralphies_cooking_basics_march7',
#     'https://calendar.colorado.edu/event/food_scarcity_in_the_forest_socio-environmental_changes_and_resilience_of_indigenous_food_system_in_the_upper_orinoco_venezuela',
#     'https://calendar.colorado.edu/event/food_scarcity_in_the_forest_socio-environmental_changes_and_resilience_of_indigenous_food_system_in_the_upper_orinoco_venezuela',
#     'https://calendar.colorado.edu/event/international_coffee_hour_1555',
#     'https://calendar.colorado.edu/event/cu_museum_reopens_discovery_corner_for_youngest_members_of_our_community_9849',
#     'https://calendar.colorado.edu/event/fall_2023_diploma_delivery_window_begins',
#     'https://calendar.colorado.edu/event/colorful_women_group_2024',
#     'https://calendar.colorado.edu/event/bipoc_yoga_2024',
#     'https://calendar.colorado.edu/event/extreme_bowling_spring24',
#     'https://calendar.colorado.edu/event/grad_endurance_seminar_series_spring_2024',
#     'https://calendar.colorado.edu/event/gpsg_rules_finance_committee',
#     'https://calendar.colorado.edu/event/conversations_on_generative_ai_in_education_and_research_8478',
#     'https://calendar.colorado.edu/event/perfect_your_resume_sp24',
#     'https://calendar.colorado.edu/event/academic_coaching_workshop',
#     'https://calendar.colorado.edu/event/mobile_food_pantry_march14',
#     'https://calendar.colorado.edu/event/altec_chinese_board_game_night',
#     'https://calendar.colorado.edu/event/chamber_orchestra_spring_2024_concert',
#     'https://calendar.colorado.edu/event/buffalo_nites_video_game_night_sp24',
#     'https://calendar.colorado.edu/event/alumni_career_transition_series_sp24',
#     'https://calendar.colorado.edu/event/coffee_with_dean_khatri',
#     'https://calendar.colorado.edu/event/buffs_after_dark_dune_mar8',
#     'https://calendar.colorado.edu/event/i_love_mondays_mar4',
#     'https://calendar.colorado.edu/event/as_career_tips_mar5',
#     'https://calendar.colorado.edu/event/engineering_employer_info_tables',
#     'https://calendar.colorado.edu/event/chinese_speech_contest',
#     'https://calendar.colorado.edu/event/feel_good_fridays_9537',
#     'https://calendar.colorado.edu/event/international_coffee_hour_1555',
#     'https://calendar.colorado.edu/event/the_play_that_goes_wrong_a_play_by_henry_lewis_jonathan_sayer_and_henry_shields',
#     'https://calendar.colorado.edu/event/snowshoe_trip',
#     'https://calendar.colorado.edu/event/foothills_hike',
#     'https://calendar.colorado.edu/event/foodie_tuesday_-_ramen_bar_wve_lobby_5230',
#     'https://calendar.colorado.edu/event/supporting_student_mental_health_1',
# ])

###

def get_data_list(): 
    data_list = []
    unique_urls = set()
    parse_page(start_url, unique_urls)       
    get_json_data(unique_urls, data_list)
    return data_list