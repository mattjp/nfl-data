import boto3
import json
import requests
import constants
import time


dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
games_table = dynamodb.Table('nfl_data_game_ids')


def validate(event):
    # TODO: add more validation
    if 'year' not in event:
        return False, f'Input must contain \'year\', event={event}'
    if 'week_start' not in event:
        return False, 'Input must contain \'week_start\''
    if 'week_end' not in event:
        return False, 'Input must contain \'week_end\''
    return True, ''


def get_team_ids(event):
    if 'team_id' in event:
        return [event['team_id']]
    else:
        return constants.ALL_TEAM_IDS.keys()


def get_season_type(season_type_url):
    return season_type_url.split("?", 1)[0][-1]


def filter_existing_game_ids(game_ids, year):
    request_items = {
        games_table.name: {
            'Keys': [{'game_id': game_id, 'year': year} for game_id in game_ids]
        }
    }

    response = dynamodb.batch_get_item(RequestItems=request_items)
    items = response['Responses']['nfl_data_game_ids']
    existing_game_ids = list(map(lambda i: i['game_id'], items))

    return list(set(game_ids) - set(existing_game_ids))


def write_game_ids(game_ids, year):
    with games_table.batch_writer() as writer:
        for game_id in game_ids:
            item = {
                'game_id': game_id,
                'year': year,
                'status': 'UNPROCESSED'
            }
            writer.put_item(Item=item)


def games_handler(event, context):
    """
    event = {
      "year": 2021,
      "team_id": 2, // optional, do all Ids if not present
      "week_start": 0,
      "week_end": 21
    }
    """
    print("RUNNING GAMES HANDLER...")

    # https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2021/teams/2/events
    # YEAR, TEAM_ID, WEEK_START, WEEK_END

    # 0. validate input
    # 1. call API
    # 2. update table with new game Ids

    event = json.loads(event['body'])
    valid, err_msg = validate(event)
    if not valid:
        return {
            'statusCode': 400,
            'body': json.dumps(err_msg)
        }

    team_ids = get_team_ids(event)
    year = int(event['year'])
    for team_id in team_ids:
        events_url = constants.EVENTS_URL.format(team_id=team_id)
        print(events_url)
        events_response = requests.get(events_url).json()
        # print(events_response)

        events_items = events_response['items']
        # print(events_items)

        item_urls = list(map(lambda item: item['$ref'], events_items))
        # print(item_urls)

        # TODO: Commenting out to save time
        game_ids = []
        for item_url in item_urls:
            print(item_url)
            time.sleep(2)
            item_response = requests.get(item_url).json()
            season_type_url = item_response['seasonType']['$ref']
            season_type_id = get_season_type(season_type_url)
            if season_type_id == constants.REG_SEASON_ID:
                game_id = item_response['id']
                game_ids.append(game_id)
        # print(game_ids)

        # TODO - need the week
        #        no we don't if we're marking games as processed in the table

        # game_ids = ['401326323', '401326129', '401326365', '401326382', '401326405', '401326413', '401326433',
        #             '401326439', '401326464', '401326482', '401326494', '401326511', '401326535', '401326552',
        #             '401326564', '401326570', '401326593']

        # Add the game_id to the database, if it is not already present.
        new_game_ids = filter_existing_game_ids(game_ids, year)
        print(new_game_ids)

        write_game_ids(new_game_ids, year)

    # TODO - implement
    #   whoops, still no implementation
    return {
        'statusCode': 200,
        'body': json.dumps('Games handler run successfully!')
    }
