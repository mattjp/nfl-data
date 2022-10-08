from aws_cdk import Stack
from constructs import Construct
from nfl_data import aggregator_service, games_service


class NflDataStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aggregator_service.AggregatorService(self, "AggregatorService")
        games_service.GamesService(self, "GamesService")
