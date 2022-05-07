import aws_cdk as core
import aws_cdk.assertions as assertions

from nfl_data.nfl_data_stack import NflDataStack

# example tests. To run these tests, uncomment this file along with the example
# resource in nfl_data/nfl_data_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NflDataStack(app, "nfl-data")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
