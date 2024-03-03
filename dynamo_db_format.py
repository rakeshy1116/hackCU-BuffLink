def convert_to_dynamodb_format(json_data):
    
    dynamodb_data = {}

    for key, value in json_data.items():
        if isinstance(value, str):
            dynamodb_data[key] = {"S": value}
        elif isinstance(value, int):
            dynamodb_data[key] = {"N": str(value)}
        elif isinstance(value, bool):
            dynamodb_data[key] = {"BOOL": value}
        elif isinstance(value, list):
            dynamodb_data[key] = {"L": [{"S": str(item)} for item in value]}
        elif isinstance(value, dict):
            dynamodb_data[key] = {"M": convert_to_dynamodb_format(value)}
        else:
            pass

    return dynamodb_data