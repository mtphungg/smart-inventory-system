import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')  

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(items, cls=DecimalEncoder),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
