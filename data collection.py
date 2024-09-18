import requests
import json
import time

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
    num_games = 0
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for game in data['results']:
                gameresponse = requests.get('https://online-go.com'+game['related']['detail'])
                if gameresponse.status_code == 200:
                    num_games += 1
                    gamedata = gameresponse.json()
                    # print('---------------')
                    my_color = 'black' if gamedata.get('black') == 513894 else 'white'
                    opponent_color = 'white' if my_color == 'black' else 'black'
                    my_historical_rating = gamedata['historical_ratings'][my_color]['ratings']['overall'].get('rating')
                    opponent_historical_rating = gamedata['historical_ratings'][opponent_color]['ratings']['overall'].get('rating')

                    result = 'win' if not gamedata.get(my_color+"_lost") else 'loss'

                    filtered_game = {
                        'id': gamedata.get('id'),  
                        'url': 'https://online-go.com/game/'+str(gamedata.get('id')),
                        # 'game_time': 1,
                        'game_type': gamedata['gamedata']['time_control'].get('speed'),
                        'moves': len(gamedata['gamedata'].get('moves')),
                        'played_date': gamedata.get('started'),
                        'result': result,
                        'me': {
                            'historical_rating': my_historical_rating,
                            'country': gamedata['historical_ratings'][my_color].get('country'),
                            'username': gamedata['players'][my_color].get('username'),
                            'color': my_color
                        },
                        'opponent': {
                            'historical_rating': opponent_historical_rating,
                            'country': gamedata['historical_ratings'][opponent_color].get('country'),
                            'username': gamedata['players'][opponent_color].get('username'),
                            'color': opponent_color
                        }
                        

                    }
                    print(f'Game {num_games}')
                    print(filtered_game)
                    games_data.append(filtered_game)
                    print('sleeping...')
                    time.sleep(2)
                    print('resuming')
            
            url = data.get('next')
            print('sleeping...')
            time.sleep(2)
            print('resuming')

        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
            break
    return games_data;


def store_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

start_time = time.time()

initial_url = 'https://online-go.com/api/v1/players/513894/games/'

filtered_games_data = get_filtered_games_data(initial_url)

store_data_to_json(filtered_games_data, 'filtered_go_games_data.json')

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Saved {len(filtered_games_data)} games to 'filtered_go_games_data.json'.")
print(f"Process took {elapsed_time:.2f / 60} minutes.")