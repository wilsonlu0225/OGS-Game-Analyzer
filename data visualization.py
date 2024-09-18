import pandas as pd
import matplotlib.pyplot as plt

games_df = pd.read_json('filtered_go_games_data.json')
# print(games_df.head())

non_correspondence_df = games_df[(games_df['game_type'] != 'correspondence') & (games_df['moves'] > 0)]

print(games_df)
print("-----------")
print(non_correspondence_df)

# wins_df = games_df[games_df['result'] == 'win']
# loss_df = games_df[games_df['result'] == 'loss']

wins_df = non_correspondence_df[non_correspondence_df['result'] == 'win']
loss_df = non_correspondence_df[non_correspondence_df['result'] == 'loss']

win_counts = wins_df.groupby('moves').size()
loss_counts = loss_df.groupby('moves').size()

plt.figure(1)
plt.plot(win_counts.index, win_counts.values, label = 'wins', color = 'green')
plt.plot(loss_counts.index, loss_counts.values, label = 'losses', color = 'red')
plt.xlabel('Number of Moves')
plt.ylabel('Number of Games')
plt.title('Moves v. Games')
plt.legend()

games_df['rating_difference'] = games_df['opponent'].apply(lambda x: x['historical_rating']) - games_df['me'].apply(lambda x: x['historical_rating'])
bins = [-float('inf'), -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, float('inf')]
# bin_labels = ['-250', '-200', '-150', '-100', '-50', '0', '50', '100', '150', '200', '250', '']
games_df['rating_difference_bin'] = pd.cut(games_df['rating_difference'], bins=bins)

games_df['win'] = games_df['result'].apply(lambda x: 1 if x == 'win' else 0)

rating_difference_df = games_df.groupby('rating_difference_bin')['win'].mean() * 100
rating_difference_df = rating_difference_df.reset_index()
rating_difference_df['bin_lower_bound'] = rating_difference_df['rating_difference_bin'].apply(lambda x: x.left)

plt.figure(2)
plt.plot(rating_difference_df['bin_lower_bound'], rating_difference_df['win'])
plt.axis((-300, 300, 0, 100))
plt.xlabel('Rating Differnece')
plt.ylabel('Win Percent')
plt.title('Rating Difference v. Win Percent')


# plt.plot(games_df['moves'], games_df['result'])
plt.show()