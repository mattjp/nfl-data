from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import games_lambda

class NflDataStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "NflDataQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        games_lambda.GamesLambda(self, "NflGamesLambda")