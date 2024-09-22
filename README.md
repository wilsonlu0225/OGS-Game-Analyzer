## OGS Game Analyzer
A program that retrieves, processes and analyzes games from the Online Go Server to find game play trends and statistics of specified player.

### Features
- Fetches and processes game data of specified player
- Stores relevant data locally on JSON files
- Visualizes statistics like games won and lost over moves to help identify potential weaknesses in each phase of the game
### How it Works
- Continually requests game data for each game
- Appends relevant game data to dictionary
- Writes all data to a local JSON file
- Loads the JSON into pandas dataframes for analysis and visualization
- Uses Matplotlib to plot various statistics
