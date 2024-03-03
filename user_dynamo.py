import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb',region_name='us-east-2')

# Define function to put user data into DynamoDB
def put_user_data(user_name, email, previousMails, extensionPrompts):
    try:
        if previousMails:
        # Define the item to be put into the DynamoDB table
            item = {
            'emailId': {'S': email},
            'userName': {'S': user_name},
            'previousMails': {"L": [{"S": str(item)} for item in previousMails]},
            'extensionPrompts': {"L": [{"S": str(item)} for item in extensionPrompts]}
        }
        
        else:
            item = {
            'emailId': {'S': email},
            'userName': {'S': user_name},
            'previousMails': {"L": []},
            'extensionPrompts': {"L": [{"S": str(item)} for item in extensionPrompts]}
        }
        
        # Put item into DynamoDB table
        response = dynamodb.put_item(
            TableName='User',
            Item=item
        )
        
        # print("User data added successfully:", response)
    
    except Exception as e:
        print("Error:", e)

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


def get_events_dynamo():
    table_name = 'NewEvents'
    
    # Example list of columns to retrieve
    columns_to_retrieve = ['hash_id', 'title', 'description']
    
    # Get specific columns from all items in DynamoDB table
    items_with_specific_columns = get_specific_columns(table_name, columns_to_retrieve)
    
    # Print all items with specific columns
    if items_with_specific_columns:
        return items_with_specific_columns
    else:
        print("Failed to retrieve items from the DynamoDB table")
        return []

def get_user_data(emailId):
    try:
        # Get item from DynamoDB table
        response = dynamodb.get_item(
            TableName='User',
            Key={
                'emailId': {'S': emailId}
            }
        )
        
        # Check if item exists
        if 'Item' in response:
            user_data = response['Item']
            # Process user data here
            # print("User data:", user_data)
            return user_data
        else:
            print("User not found")
            return None
    
    except Exception as e:
        print("Error:", e)

# Example usage
def test():
    user_name = "John Doe"
    email = "john.doe@example.com"
    previousMails = ["hash1","hash2"]
    extensionPrompts = ["text1","text2"]
    # Call function to put user data into DynamoDB
    put_user_data(user_name, email, previousMails, extensionPrompts)
