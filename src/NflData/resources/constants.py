from team import Team

# Teams
ALL_TEAM_IDS = {
    1: Team('Atlanta', 'Falcons', 'ATL'),
    2: Team('Buffalo', 'Bills', 'BUF'),
    3: Team('Chicago', 'Bears', 'CHI'),
    4: Team('Cincinnati', 'Bengals', 'CIN'),
    5: Team('Cleveland', 'Browns', 'CLE'),
    6: Team('Dallas', 'Cowboys', 'DAL'),
    7: Team('Denver', 'Broncos', 'DEN'),
    8: Team('Detroit', 'Lions', 'DET'),
    9: Team('Green Bay', 'Packers', 'GB'),
    10: Team('Tennessee', 'Titans', 'TEN'),
    11: Team('Indianapolis', 'Colts', 'IND'),
    12: Team('Kansas City', 'Chiefs', 'KC'),
    13: Team('Las Vegas', 'Raiders', 'LV'),
    14: Team('Los Angeles', 'Rams', 'LAR'),
    15: Team('Miami', 'Dolphins', 'MIA'),
    16: Team('Minnesota', 'Vikings', 'MIN'),
    17: Team('New England', 'Patriots', 'NE'),
    18: Team('New Orleans', 'Saints', 'NO'),
    19: Team('New York', 'Giants', 'NYG'),
    20: Team('New York', 'Jets', 'NYJ'),
    21: Team('Philadelphia', 'Eagles', 'PHI'),
    22: Team('Arizona', 'Cardinals', 'ARI'),
    23: Team('Pittsburgh', 'Steelers', 'PIT'),
    24: Team('Los Angeles', 'Chargers', 'LAC'),
    25: Team('San Fransisco', '49ers', 'SF'),
    26: Team('Seattle', 'Seahawks', 'SEA'),
    27: Team('Tampa Bay', 'Buccaneers', 'TB'),
    28: Team('Washington', 'Commanders', 'WSH'),
    29: Team('Carolina', 'Panthers', 'CAR'),
    30: Team('Jacksonville', 'Jaguars', 'JAX'),
    33: Team('Baltimore', 'Ravens', 'BAL'),
    34: Team('Houston', 'Texans', 'HOU')
}

# Urls
EVENTS_URL = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2021/teams/{team_id}/events'

# Season types
PRE_SEASON_ID = "1"
REG_SEASON_ID = "2"
POST_SEASON_ID = "3"

