import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

ses = boto3.client('ses', region_name='us-east-2')
 

def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']

    reorder_items = [item for item in items if int(item['stock']) < int(item['reorder_point'])]

    if reorder_items:
        message_body = "The following items need to be reordered:\n\n"
        for item in reorder_items:
            message_body += f"- {item['name']} (Stock: {item['stock']}, Reorder Point: {item['reorder_point']})\n"

        # Send email
        ses.send_email(
            Source='lucie.phung0205@gmail.com',  
            Destination={'ToAddresses': ['lucie.phung0205@gmail.com']},  
            Message={
                'Subject': {'Data': '🚨 Low Stock Alert'},
                'Body': {'Text': {'Data': message_body}}
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps({'reorder_needed': reorder_items}, default=str)
    }
