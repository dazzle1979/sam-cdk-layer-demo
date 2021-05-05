from aws_cdk import (
    aws_lambda as lambda_,
    core
)


class LambdaStack(core.NestedStack):

    def __init__(
        self,
        scope: core.Construct,
        construct_id: str,
        params: object,
        **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function: test local invoke
        test_function = lambda_.Function(
            id='test-function',
            scope=self,
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset('lambda/src'),
            handler='lambda.handler',
            layers=[
                params['test_layer']
            ],
            environment={
                'LOG_LEVEL': 'INFO',
                'POWERTOOLS_SERVICE_NAME': 'test'
            }
        )
