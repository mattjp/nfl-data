import aws_cdk as cdk
from constructs import Construct


class AggregatorService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        lambda_role = cdk.aws_iam.Role(
            self,
            "AggregatorLambdaRole",
            assumed_by=cdk.aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Role used by aggregator lambda function.",
            managed_policies=[
                cdk.aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                cdk.aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess")
            ]
        )

        handler = cdk.aws_lambda.Function(
            self,
            "AggregatorHandler",
            runtime=cdk.aws_lambda.Runtime.PYTHON_3_7,
            code=cdk.aws_lambda.Code.from_asset("resources"),
            handler="aggregator.aggregator_handler",
            role=lambda_role,
            timeout=cdk.Duration.seconds(900)  # Max time
        )

        api = cdk.aws_apigateway.RestApi(
            self,
            "AggregatorApi",
            rest_api_name="NFL Data Game Aggregator Service",
            description="This service will get aggregate statistics for a given game."
        )

        aggregator_integration = cdk.aws_apigateway.LambdaIntegration(
            handler,
            request_templates={
                "application/json": "{ \"statusCode\": \"200\" }"
            }
        )

        games = api.root.add_resource("aggregate")
        games.add_method("POST", aggregator_integration)  # make this a POST; add uri slug
