#!/usr/bin/env python3

from aws_cdk import core

from sam_cdk_layer_demo.sam_cdk_layer_demo_stack import SamCdkLayerDemoStack
from sam_cdk_layer_demo.lambda_stack import LambdaStack
from sam_cdk_layer_demo.layer_stack import LayerStack


app = core.App()
sam_cdk_layer_demo_stack = SamCdkLayerDemoStack(app, 'sam-cdk-layer-demo')

layer_stack = LayerStack(sam_cdk_layer_demo_stack, 'layer-stack')

lambda_stack = LambdaStack(
    sam_cdk_layer_demo_stack, 'lambda-stack',
    params={
        'test_layer': layer_stack.test_layer
    }
)

app.synth()
