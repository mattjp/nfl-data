import aws_cdk as cdk
from constructs import Construct


class GamesService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        lambda_role = cdk.aws_iam.Role(
            self,
            "GamesLambdaRole",
            assumed_by=cdk.aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role used by games lambda function.",
            managed_policies=[
                cdk.aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                cdk.aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
            ]
        )

        handler = cdk.aws_lambda.Function(
            self,
            "GamesHandler",
            runtime=cdk.aws_lambda.Runtime.PYTHON_3_7,
            code=cdk.aws_lambda.Code.from_asset("resources"),
            handler="games.games_handler",
            role=lambda_role,
            timeout=cdk.Duration.seconds(900)  # Enough time to calculate entire season for all teams
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

        games = api.root.add_resource("games")
        games.add_method("POST", get_games_integration)  # make this a POST; add uri slug

