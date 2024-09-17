import requests

response = requests.get('https://online-go.com/api/v1/players/513894/games/')
# print(response)
if response.status_code == 200:
    data = response.json()
    # print(f"{response.status_code}")
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")