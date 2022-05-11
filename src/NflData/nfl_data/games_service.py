import aws_cdk as cdk
from constructs import Construct


class GamesService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        handler = cdk.aws_lambda.Function(
            self,
            "GamesHandler",
            runtime=cdk.aws_lambda.Runtime.PYTHON_3_9,
            code=cdk.aws_lambda.Code.from_asset("resources"),
            handler="games.games_handler"
        )

        api = cdk.aws_apigateway.RestApi(
            self,
            "GamesApi",
            rest_api_name="NFL Data Games Service",
            description="This service will get NFL game ids for a range of weeks in a given year."
        )

        get_games_integration = cdk.aws_apigateway.LambdaIntegration(
            handler,
            request_templates={
                "application/json": "{ \"statusCode\": \"200\" }"
            }
        )

        api.root.add_method("GET", get_games_integration)

