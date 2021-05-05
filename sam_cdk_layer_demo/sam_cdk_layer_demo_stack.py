from aws_cdk import (
    aws_lambda as lambda_,
    core
)


class SamCdkLayerDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Layer containing all the related third party imports
        test_layer_same_stack = lambda_.LayerVersion(
            self, 'layer-test-same-stack',
            code=lambda_.Code.asset('lambda/layers/test_layer'),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_8],
            description='Test Layer'
        )

        # Lambda function: test local invoke
        test_function_same_stack = lambda_.Function(
            id='test-function-same-stack',
            scope=self,
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset('lambda/src'),
            handler='lambda.handler',
            layers=[
                test_layer_same_stack
            ],
            environment={
                'LOG_LEVEL': 'INFO',
                'POWERTOOLS_SERVICE_NAME': 'test'
            }
        )
