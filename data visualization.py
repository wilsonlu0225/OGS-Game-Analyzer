# import json
import pandas as pd
import matplotlib.pyplot as plt

games_df = pd.read_json('filtered_go_games_data.json')
print(games_df.head())

