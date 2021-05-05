# Import from layer
import yaml

def handler(event, context):
    # Do something with PyYaml
    document = """
        a: 1
        b:
            c: 3
            d: 4
    """
    print(yaml.load(document))
    return {
        'StatusCode': 200
    }