import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb',region_name='us-east-2')

# Define function to get all items from DynamoDB table
def get_all_items(table_name):
    try:
        # Initialize list to store items
        all_items = []
        
        # Start scanning the table
        response = dynamodb.scan(
            TableName=table_name
        )
        
        # Continue scanning if there are more items
        while 'LastEvaluatedKey' in response:
            all_items.extend(response['Items'])
            response = dynamodb.scan(
                TableName=table_name,
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
        
        # Add the remaining items
        all_items.extend(response['Items'])
        
        return all_items
    
    except Exception as e:
        print("Error:", e)
        return None

# Example usage
if __name__ == "__main__":
    # Example table name
    table_name = 'NewEvents'
    
    # Get all items from DynamoDB table
    all_items = get_all_items(table_name)
    
    # Print all items
    if all_items:
        for item in all_items:
            print(item)
            print('\n')
    else:
        print("Failed to retrieve items from the DynamoDB table")
