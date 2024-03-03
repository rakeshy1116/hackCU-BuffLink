import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb',region_name='us-east-2')

# Define function to get specific columns from all items in DynamoDB table
def get_specific_columns(table_name, columns):
    try:
        # Initialize list to store items
        all_items = []
        
        # Start scanning the table with ProjectionExpression
        response = dynamodb.scan(
            TableName=table_name,
            ProjectionExpression=','.join(columns)
        )
        
        # Continue scanning if there are more items
        while 'LastEvaluatedKey' in response:
            all_items.extend(response['Items'])
            response = dynamodb.scan(
                TableName=table_name,
                ProjectionExpression=','.join(columns),
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
    
    # Example list of columns to retrieve
    columns_to_retrieve = ['hash_id', 'title', 'description']
    
    # Get specific columns from all items in DynamoDB table
    items_with_specific_columns = get_specific_columns(table_name, columns_to_retrieve)
    
    # Print all items with specific columns
    if items_with_specific_columns:
        for item in items_with_specific_columns:
            print(item)
    else:
        print("Failed to retrieve items from the DynamoDB table")
