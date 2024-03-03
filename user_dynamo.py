import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb',region_name='us-east-2')

# Define function to put user data into DynamoDB
def put_user_data(user_name, email, previousMails, extensionPrompts):
    try:
        # Define the item to be put into the DynamoDB table
        item = {
            'emailId': {'S': email},
            'userName': {'S': user_name},
            'previousMails': {"L": [{"S": str(item)} for item in previousMails]},
            'extensionPrompts': {"L": [{"S": str(item)} for item in extensionPrompts]}
        }
        
        # Put item into DynamoDB table
        response = dynamodb.put_item(
            TableName='User',
            Item=item
        )
        
        print("User data added successfully:", response)
    
    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    user_name = "John Doe"
    email = "john.doe@example.com"
    previousMails = ["hash1","hash2"]
    extensionPrompts = ["text1","text2"]
    # Call function to put user data into DynamoDB
    put_user_data(user_name, email, previousMails, extensionPrompts)
