import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('NewEvents')
partition_key = 'hash_id'

def fetch_event_data_from_dynamo(events_hash_ids):

    try:
        # Define the item to be put into the DynamoDB table
        event_data_list = []

        for event_hash_id in events_hash_ids:

            event_data = table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key(partition_key).eq(event_hash_id)
            )

            if event_data is not None:
                event_data_list.extend(event_data['Items'])
        
        return event_data_list
    
    except Exception as e:

        print("Error:", e)

# result = fetch_event_data_from_dynamo(['3757ef7b91b47c15c49c75d97dc6a839e3d5996b201b4748964b2c399d0ecc09d6694e47a41d0053341a13eb6d0b8897baf8d6ba64b7e68298239ae70ef31e32'])
# print(result)