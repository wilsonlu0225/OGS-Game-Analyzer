import pandas as pd
import matplotlib.pyplot as plt

games_df = pd.read_json('filtered_go_games_data.json')
# print(games_df.head())

# print("-----------")
print(games_df)

wins_df = games_df[games_df['result'] == 'win']
loss_df = games_df[games_df['result'] == 'loss']

win_counts = wins_df.groupby('moves').size()
loss_counts = loss_df.groupby('moves').size()

plt.plot(win_counts.index, win_counts.values, label = 'wins', color = 'green')
plt.plot(loss_counts.index, loss_counts.values, label = 'losses', color = 'red')
plt.xlabel('Number of Moves')
plt.ylabel('Number of Games')
plt.title('Moves v. Games')
plt.legend()


# plt.plot(games_df['moves'], games_df['result'])
plt.show()