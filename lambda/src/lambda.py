from aws_lambda_powertools import Logger

logger = Logger()

def handler(event, context):
    logger.info("Logging with powertools from layer")
    return {
        'StatusCode': 200
    }