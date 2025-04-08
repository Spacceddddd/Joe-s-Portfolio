# I wrote this in Google colab so please bear with me


import pandas as pd
file_paths = ['/content/drive/MyDrive/archive/matches/matches/euro/1960.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1964.csv','/content/drive/MyDrive/archive/matches/matches/euro/1968.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1972.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1976.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1980.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1984.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1988.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1992.csv', '/content/drive/MyDrive/archive/matches/matches/euro/1996.csv',  '/content/drive/MyDrive/archive/matches/matches/euro/2000.csv', '/content/drive/MyDrive/archive/matches/matches/euro/2004.csv', '/content/drive/MyDrive/archive/matches/matches/euro/2008.csv' , '/content/drive/MyDrive/archive/matches/matches/euro/2012.csv', '/content/drive/MyDrive/archive/matches/matches/euro/2016.csv', '/content/drive/MyDrive/archive/matches/matches/euro/2020.csv', '/content/drive/MyDrive/archive/matches/matches/euro/2024.csv']  # Add all your CSV file paths here
df = pd.concat((pd.read_csv(file, low_memory=False) for file in file_paths), ignore_index=True)
away_appearances = df['away_team'].value_counts().get('France', 0)
home_appearances = df['home_team'].value_counts().get('France', 0)
Total = away_appearances + home_appearances

print(f"The total number of appearances made by Les Bleus at the Euros is {Total}")

---------------------------------------------------------------------------------------
france = df[(df['home_team'] == 'France') | (df['away_team'] == "France")]
---------------------------------------------------------------------------------------
france_matches_away = df[df['away_team'] == 'France']
france_matches_away
----------------------------------------------------------------------------------------
away_scores = france_matches_away['away_score'].sum()
print(round(away_scores))
----------------------------------------------------------------------------------------
france_matches_home = df[df['home_team'] == 'France']
france_matches_home
--------------------------------------------------------------------------------------
home_scores = france_matches_home['home_score'].sum()
print(round(home_scores))
----------------------------------------------------------------------------------------
england_away = df[(df['away_team'] == "England") & (df['home_team'] == 'France')]
england_away
-------------------------------------------------------------------------------------
france_matches_home
------------------------------------------------------------------------------------
# Extracting the coach name from the string
france_matches_home['home_coach'] = france_matches_home['home_coaches'].str.extract(r"'name': '([^']*)'")
france_matches_home['away_coach'] = france_matches_home['away_coaches'].str.extract(r"'name': '([^']*)'")

# Dropping unnecessary columns
francehomematches = france_matches_home.drop(
    ['id_match', 'home_score_total', 'stadium_name_event', 'home_lineups', 'away_lineups', 'events',
     'home_coaches', 'away_coaches', 'stadium_name', 'stadium_name_sponsor', 'away_score_total'], axis=1
)

# Ensure there are no NaN values in home_score and away_score columns
francehomematches['home_score'] = francehomematches['home_score'].fillna(0)  # Or use .fillna(0) or another value depending on your data
francehomematches['away_score'] = francehomematches['away_score'].fillna(0)  # Or use .fillna(0) or another value depending on your data

# Rounding the home_score and away_score
francehomematches['home_score'] = round(francehomematches['home_score']).astype(int)  # Cast to int after rounding
francehomematches['away_score'] = round(francehomematches['away_score']).astype(int)  # Cast to int after rounding

# Create the 'total_score' column by concatenating home_score and away_score as integers (no decimal)
francehomematches['total_score'] = francehomematches['home_score'].astype(str) + ":" + francehomematches['away_score'].astype(str)

# Display the resulting DataFrame
france = france.drop(
    ['id_match', 'home_score_total', 'stadium_name_event', 'home_lineups', 'away_lineups', 'events',
     'home_coaches', 'away_coaches', 'stadium_name', 'stadium_name_sponsor', 'away_score_total', 'goals',
     'penalties_missed','penalties','red_cards','game_referees','stadium_latitude','stadium_longitude',
     'stadium_pitch_length'	,'stadium_pitch_width'], axis=1
)

france['home_score'] = round(france['home_score']).astype(int)  # Cast to int after rounding
france['away_score'] = round(france['away_score']).astype(int)  # Cast to int after rounding
france

