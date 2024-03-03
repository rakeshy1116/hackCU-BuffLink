import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

# Define function to put user data into DynamoDB
def upload_to_dynamo(data_list):
    try:
        # Define the item to be put into the DynamoDB table
        item_list = data_list

        for item in item_list:
        
            # Put item into DynamoDB table
            response = dynamodb.put_item(
                TableName = 'NewEvents',
                Item = item
            )
        
        #print("User data added successfully:", response)
    
    except Exception as e:

        print("Error:", e)
