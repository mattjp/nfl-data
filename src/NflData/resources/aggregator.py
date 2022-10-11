import boto3
import constants
from botocore.errorfactory import ClientError
import json
import requests

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
s3 = boto3.resource('s3', region_name='us-east-2')

BUCKET = 'data-nfl'


def game_data_in_s3(year, game_id):
    try:
        s3.Object(BUCKET, f"raw/{year}/{game_id}").load()
        return True
    except ClientError:
        return False


def write_game_data_to_s3(year, game_id):
    game_url = constants.GAME_URL.format(game_id=game_id, limit=400)
    print(game_url)
    game_response = requests.get(game_url).json()
    game_items = game_response["items"]
    s3.Object(BUCKET, f"raw/{year}/{game_id}").put(Body=json.dumps(game_items))


def get_game_data_from_s3(year, game_id):
    print(f"Reading data for game_id={game_id} from S3.")
    raw_content = s3.Object(BUCKET, f"raw/{year}/{game_id}").get()["Body"].read().decode("utf-8")
    return json.loads(raw_content)


def process_item(item):
    """
    1. Remove invalid items (coin toss, kickoff, etc.)
    2. Process the play string


    :param item:
    :return:
    """
    pass


def aggregator_handler(event, context):
    """
    Aggregate statistics for a given game.

    1. If the raw game data is not in S3, add it to S3.
       s3://data-nfl/raw/$YEAR/$GAME_ID
    2. Read raw game data from S3.
    3. Process each play and aggregate stats locally.
    4. Write all stats to DynamoDB after processing.
       team_off_stats_by_down_$YEAR
       team_def_stats_by_down_$YEAR
    5. Mark the game as processed in DynamoDB. TODO: this should be done by handler

    :param event:
        "body": {
            "year": 2021,
            "game_id": 0123456789
        }
    :param context:
    :return:
    """

    body = json.loads(event['body'])
    year = body['year']
    game_id = body['game_id']

    if not game_data_in_s3(year, game_id):
        print(f"Game data for game_id={game_id} not present, fetching and writing to S3...")
        write_game_data_to_s3(year, game_id)

    game_data = get_game_data_from_s3(year, game_id)
    # print(game_data)

    # for item in game_data['items']:
    #     process_item(item)





    return {
        'statusCode': 200,
        'body': json.dumps('Aggregator run successful!')
    }
