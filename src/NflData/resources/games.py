import json
import requests
import constants


# ALL_TEAM_IDS = range(1, )

def validate(event) -> tuple[bool, str]:
    # TODO: add more validation
    if 'year' not in event:
        return False, 'Input must contain \'year\''
    if 'week_start' not in event:
        return False, 'Input must contain \'week_start\''
    if 'week_end' not in event:
        return False, 'Input must contain \'week_end\''
    return True, ''


def get_team_ids(event) -> list[int]:
    if 'team_id' in event:
        return [event['team_id']]
    else:
        return constants.ALL_TEAM_IDS.keys()


def games_handler(event, context):
    """
    event = {
      "year": 2021,
      "team_id": 2, // optional, do all Ids if not present
      "week_start": 0,
      "week_end": 18
    }
    """

    # https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2021/teams/2/events
    # YEAR, TEAM_ID, WEEK_START, WEEK_END

    # 0. validate input
    # 1. call API
    # 2. update table with new game Ids

    valid, err_msg = validate(event)
    if not valid:
        return {
            'statusCode': 400,
            'body': json.dumps(err_msg)
        }

    team_ids = get_team_ids(event)
    for team_id in team_ids:
        url = constants.GAMES_URL.format(team_id=team_id)
        print(url)
        # requests.get(url)



    # TODO - implement
    return {
        'statusCode': 200,
        'body': json.dumps('Games handler running!')
    }