import requests
import json

import pandas as pd

# # response = requests.get('https://online-go.com/api/v1/players/513894/games/')
# # print(response)
# if response.status_code == 200:
#     data = response.json()
#     # print(f'{response.status_code}')
#     print(data)
# else:
#     print(f'Failed to retrieve data. Status code: {response.status_code}')

def get_filtered_games_data(url):
    games_data = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for game in data['results']:
                gameresponse = requests.get('https://online-go.com'+game['related']['detail'])
                if gameresponse.status_code == 200:
                    gamedata = gameresponse.json()
                    # print('---------------')

                    filtered_game = {

                        'id': gamedata.get('id'),  
                        'url': 'https://online-go.com/game/'+str(gamedata.get('id')),
                        # 'game_time': 1,
                        'game_type': gamedata['gamedata']['time_control'].get('speed'),
                        'moves': len(gamedata['gamedata'].get('moves')),
                        'played_date': gamedata.get('started')

                    }
                    games_data.append(filtered_game)
            
            url = data.get('next')

        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
            break
    return games_data;


def store_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


initial_url = 'https://online-go.com/api/v1/players/513894/games/'

filtered_games_data = get_filtered_games_data(initial_url)

store_data_to_json(filtered_games_data, 'filtered_go_games_data.json')
print(f"Saved {len(filtered_games_data)} games to 'filtered_go_games_data.json'.")

