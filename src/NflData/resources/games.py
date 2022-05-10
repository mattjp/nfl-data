import json

def games_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Games handler running!')
    }