from aws_cdk import (
    aws_lambda as lambda_,
    core
)


class LayerStack(core.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Layer containing all the related third party imports
        self.test_layer = lambda_.LayerVersion(
            self, 'layer-test',
            code=lambda_.Code.asset('lambda/layers/test_layer'),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_8],
            description='Test Layer'
        )