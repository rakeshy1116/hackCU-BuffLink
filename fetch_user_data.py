import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('User')
partition_key = 'emailId'

def fetch_user_data_from_dynamo(user_email):

    try:
        # Define the item to be put into the DynamoDB table
        user_data = table.query(
             KeyConditionExpression=boto3.dynamodb.conditions.Key(partition_key).eq(user_email)
        )
        
        return user_data['Items'][0]
    
    except Exception as e:

        print("Error:", e)

# print(fetch_user_data_from_dynamo('yrakeshchowdary1116@gmail.com'))